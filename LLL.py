import rsa
import thrift
import requests
import json

from thrift.protocol import TCompactProtocol
from thrift.transport import THttpClient
import TalkService
import LineLoginService
from ttypes import LoginRequest

import pyqrcode

_session = requests.session()

def getJson(url, headers=None):
    if headers is None:
            return json.loads(_session.get(url).text)
    else:
            return json.loads(_session.get(url, headers=headers).text)
                        
def print_qr(uri):
    print(pyqrcode.create(uri).terminal('green', 'white', 1))

class LLL(object):
  
    UA = "Line/7.14.0 iPad5,1 10.2.0"
    LA = "IOSIPAD\t7.14.0\tiPhone OS\t10.12.0"

    auth_query_path = "/api/v4/TalkService.do"
    http_query_path = "/S4"
    login_query_path = "/api/v4p/rs"
    wait_for_mobile_path = "/Q"
    host = "gd2.line.naver.jp"
    port = 443

    def __init__(self):
        # self.transport = THttpClient.THttpClient(LLL.host, LLL.port, LLL.http_query_path)
        self.transport = THttpClient.THttpClient("https://" + LLL.host + ":" +  str(LLL.port) + LLL.http_query_path)
        self.transport.setCustomHeaders({
            "User-Agent" : LLL.UA,
            "X-Line-Application" : LLL.LA,
            "X-LHM" : "POST",
            "x-lal" : "ja-JP_JP"
        })
        self.protocol = TCompactProtocol.TCompactProtocol(self.transport)
        self.login_client = LineLoginService.Client(self.protocol)
        self.client = TalkService.Client(self.protocol)

        self.transport.open()

        self.qr_login()

    def qr_login(self):
        self.transport.path = LLL.auth_query_path
        qrcode = self.client.getAuthQrcode(keepLoggedIn=1, systemName='LLL')
        url = "line://au/q/" + qrcode.verifier 
        print_qr(url)
        
        header = { 
                'User-Agent': LLL.UA, 
                'X-Line-Application': LLL.LA, 
                'x-lal' : 'ja-US_US',
                'x-lpqs' : LLL.auth_query_path,
                'X-Line-Access': qrcode.verifier }
        
        getAccessKey = getJson('https://' + LLL.host + LLL.wait_for_mobile_path, header)

        self.transport.path = LLL.login_query_path
        req = LoginRequest()
        req.type = 1
        req.verifier = qrcode.verifier
        req.e2eeVersion = 1
        print(req)

        res = self.login_client.loginZ(req)
 
        self.authToken = res.authToken
        self.certificate = res.certificate       
 
        self.transport.setCustomHeaders({
               "User-Agent" : LLL.UA,
               "X-Line-Application" : LLL.LA,
               "X-Line-Access" : self.authToken
        })

        self.transport.path = LLL.http_query_path
 

    def setup_by_normal_login(self, userid, password):
        # currently not working correctly since I'm too lazy to analyze this feature so use qr login instead

        self.userid = userid
        self.password = password

        self.transport.path = LLL.auth_query_path
        r = self.login_client.getRSAKeyInfo(IdentityProvider.LINE)

        data = (chr(len(r.sessionKey)) + r.sessionKey 
                + chr(len(self.userid)) + self.userid 
                + chr(len(self.password)) + self.password)

        pub = rsa.PublicKey(int(r.nvalue, 16), int(r.evalue, 16))
        cipher = rsa.encrypt(data, pub).encode('hex')

        login_request = loginRequest()
        login_request.type = 0
        login_request.identityProvider = IdentityProvider.LINE
        login_request.identifier = r.keynm
        login_request.password = cipher
        login_request.keepLoggedIn = 1
        login_request.accessLocation = "127.0.0,1"
        login_request.systemName = "LLL"
        login_request.e2eeVersion = 1

        self.transport.path = LLL.login_query_path
        r = self.login_client.loginZ(login_request)

        if r.type == LoginResultType.SUCCESS:
           self.authToken = r.authToken
           self.certificate = r.certificate;

           self.transport.setCustomHeaders({
               "User-Agent" : LLL.UA,
               "X-Line-Application" : LLL.LA,
               "X-Line-Access" : self.authToken
           })

        elif r.type == LoginResultType.REQUIRE_QRCODE:
           # im not aware of this feature
           pass

        elif r.type == LoginResultType.REQUIRE_DEVICE_CONFIRM:
           print("the pincode is {}".format(r.pinCode))
           verifier = requests.get(url="http://gd2.line.naver.jp/Q", headers={ "X-Line-Access" : r.verifier }).json()["result"]["verifier"].encode("utf-8")
          
           # verifier_request = loginRequest()
           # verifier_request.verifier = verifier
           # r = self.login_client.loginZ(verifier_request)
            
           self.transport.path = LLL.auth_query_path
           r = self.login_client.loginWithVerifierForCertificate(verifier)

           self.authToken = r.authToken
           self.certificate = r.certificate

        else:
           print("unimplemented functionality {}".format(r.type))

        self.transport.path = LLL.http_query_path

