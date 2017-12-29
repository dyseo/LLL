import rsa
import thrift
import requests

from thrift.transport import THttpClient
from thrift.protocol import TCompactProtocol

from Gen.line import LineService
from Gen.line.ttypes import *


class LLL(object):
  
    UA = "Line/7.9.0 iPad4,1 9.3.3"
    LA = "IOSIPAD\t7.9.0\tiPhone OS\t9.3.3"

    auth_query_path = "/api/v4/TalkService.do"
    http_query_path = "/S4"
    login_query_path = "/api/v4p/rs"
    wait_for_mobile_path = "/Q"
    host = "gd2.line.naver.jp"
    port = 443

    def __init__(self):
        self.transport = THttpClient.THttpClient(LLL.host, LLL.port, LLL.http_query_path)
        # self.transport = THttpClient.THttpClient("http://" + LLL.host + ":" +  str(LLL.port) + LLL.http_query_path)
        self.transport.setCustomHeaders({
            "User-Agent" : LLL.UA,
            "X-Line-Application" : LLL.LA,
            "X-LHM" : "POST",
            "x-lal" : "ja-JP_JP"
        })
        self.protocol = TCompactProtocol.TCompactProtocol(self.transport)
        self.client = LineService.Client(self.protocol)

        self.transport.open()
    
    def setup_by_normal_login(self, userid, password):
       self.userid = userid
       self.password = password

       self.transport.path = LLL.auth_query_path
       r = self.client.getRSAKeyInfo(IdentityProvider.LINE)
       
       data = (chr(len(r.sessionKey)) + r.sessionKey 
                + chr(len(self.userid)) + userid 
                + chr(len(self.password)) + password)
       
       pub = rsa.PublicKey(int(r.nvalue, 16), int(r.evalue, 16))
       cipher = rsa.encrypt(data, pub).encode('hex')

       login_request = loginRequest()
       login_request.type = 0
       login_request.identityProvider = IdentityProvider.LINE
       login_request.password = cipher
       login_request.keepLoggedIn = 1
       login_request.accessLocation = "127.0.0,1"
       login_request.systemName = "LLL"
       login_request.e2eeVersion = 1

       self.transport.path = LLL.login_query_path
       r = self.client.loginZ(login_request)
      
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
           verifier = requests.get(url="http://gd2.line.naver.jp/Q", headers={ "X-Line-Access" : r.verifier }).json()["result"]["verifier"]
           login_request.verifier = verifier
           r = self.client.loginZ(login_request)

           self.authToken = r.authToken
           self.certificate = r.certificate

       else:
           print("unimplemented functionality {}".format(r.type))

       self.transport.path = LLL.http_query_path

