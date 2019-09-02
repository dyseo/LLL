import pyqrcode
import requests
import json
import os
import rsa
import thriftpy2
from thriftpy2.http import THttpClient
from thriftpy2.protocol import TCompactProtocol
from thriftpy2.thrift import TClient

class LineClient(object):
    
    def __init__(self):
        self.line_thrift = thriftpy2.load(
            os.path.dirname(__file__) + "/line.thrift", module_name="line_thrift")

        self.transport = THttpClient("https://gd2.line.naver.jp:443")
        self.transport.setCustomHeaders({
            "User-Agent": "Line/7.14.0 iPad5,1 10.2.0",
            "X-Line-Application": "IOSIPAD\t7.14.0\tiPhone OS\t10.12.0",
            "X-LHM": "POST",
            "X-lal": "ja-JP_JP"
        })
        self.protocol = TCompactProtocol(self.transport)
        self.transport.open()
        self.client = TClient(self.line_thrift.LineService, self.protocol)
        self._session = requests.session()
        
    def __write_val(self, data):
        return (chr(len(data)) + data)

    def __gen_message(self, tuple_msg):
        return (''.join(tuple_msg)).encode('utf-8')

    def __rsa_crypt(self, message,RSA):
        pub_key = rsa.PublicKey(int(RSA.nvalue, 16), int(RSA.evalue, 16))
        crypto  = rsa.encrypt(message, pub_key)
        return crypto

    def _encryptedEmailAndPassword(self, mail, passwd, RSA):
        message_ = (
			self.__write_val(RSA.sessionKey),
			self.__write_val(mail),
			self.__write_val(passwd),
        )
        message = self.__gen_message(message_)
        crypto  = self.__rsa_crypt(message, RSA).hex()
        return crypto

    def wait_for_confirm(self, verifier):
        r = requests.get("https://gd2.line.naver.jp/Q", headers={
        		"User-Agent": LEGY_ENDPOINT.UA,
        		"X-Line-Application": LEGY_ENDPOINT.LA,
        		"x-lal": "ja-US_US",
        		"x-lpqs": LEGY_ENDPOINT.REGISTRATION,
			"X-Line-Access": verifier
        })
        return r.json()
 
    def email_login(self, email, password, cert=None):
        self.transport.path = LEGY_ENDPOINT.REGISTRATION
        rsa_key = self.client.getRSAKeyInfo(1)
        crypt  = self._encryptedEmailAndPassword(email, password, rsa_key)
        self.transport.path = LEGY_ENDPOINT.AUTH_REGISTRATION
        req = self.line_thrift.loginRequest()
        req.type = 0
        req.identityProvider = 3
        req.identifier = rsa_key.keynm
        req.password = crypt
        req.keepLoggedIn = True
        req.accessLocation = "127.0.0.0"
        req.systemName = "LLL"
        req.certificate = cert
        req.verifier = None
        req.secret = crypt.encode() if type(crypt) == str else crypt
        req.e2eeVersion = 2
        result = self.client.loginZ(req)
        self.transport.path = LEGY_ENDPOINT.REGISTRATION
        if result.type == 3:
            print("Check your phone and input this pin %s"% (result.pinCode))
            r = self.wait_for_confirm(result.verifier)
            req = self.line_thrift.loginRequest(
				1,
				1,
				None, None, True,
				"127.0.0.0",
				"LLL",
				cert, r['result']['verifier'],
				None, 
				2
            	)
            self.transport.path = LEGY_ENDPOINT.AUTH_REGISTRATION
            result = self.client.loginZ(req)
            self.authToken = result.authToken
            self.certificate = result.certificate
            self.transport.setCustomHeaders({
            	"User-Agent": LEGY_ENDPOINT.UA,
            	"X-Line-Application": LEGY_ENDPOINT.LA,
            	"X-Line-Access": self.authToken
           })
        if result.type == 1:
            self.transport.path = LEGY_ENDPOINT.AUTH_REGISTRATION
            result = self.client.loginZ(req)
            self.authToken = result.authToken
            self.certificate = result.certificate
            self.transport.setCustomHeaders({
            	"User-Agent": LEGY_ENDPOINT.UA,
            	"X-Line-Application": LEGY_ENDPOINT.LA,
            	"X-Line-Access": self.authToken
           })
           
        self.transport.path = LEGY_ENDPOINT.NORMAL
           
    def qr_login(self):
        self.transport.path = LEGY_ENDPOINT.REGISTRATION
        qrcode = self.client.getAuthQrcode(keepLoggedIn=1, systemName='LLL')
        url = "line://au/q/" + qrcode.verifier
        #Some user have confuced using Qrcode, so just print URL
        print(url)
        getAccessKey = self.wait_for_confirm(qrcode.verifier)
        self.transport.path = LEGY_ENDPOINT.AUTH_REGISTRATION
        req = self.line_thrift.loginRequest()
        req.type = 1
        req.verifier = qrcode.verifier
        req.e2eeVersion = 1

        res = self.client.loginZ(req)

        self.authToken = res.authToken
        self.certificate = res.certificate

        self.transport.setCustomHeaders({
            "User-Agent": LEGY_ENDPOINT.UA,
            "X-Line-Application": LEGY_ENDPOINT.LA,
            "X-Line-Access": self.authToken
        })

        self.transport.path = LEGY_ENDPOINT.NORMAL


class LEGY_ENDPOINT(object):

    UA = "Line/7.14.0 iPad5,1 10.2.0"
    LA = "IOSIPAD\t7.14.0\tiPhone OS\t10.12.0"

    LONG_POLLING = "/P4"
    NORMAL_POLLING = "/NP4"
    NORMAL = "/S4"
    COMPACT_MESSAGE = "/C5"
    REGISTRATION = "/api/v4/TalkService.do"
    NOTIFY_SLEEP = "/F4"
    NOTIFY_BACKGROUND = "/B"
    BUDDY = "/BUDDY4"
    SHOP = "/SHOP4"
    UNIFIED_SHOP = "/TSHOP4"
    STICON = "/SC4"
    CHANNEL = "/CH4"
    CANCEL_LONGPOLLING = "/CP4"
    SNS_ADAPTER = "/SA4",
    SNS_ADAPTER_REGISTRATION = "/api/v4p/sa"
    USER_INPUT = ""
    USER_BEHAVIOR_LOG = "/L1"
    AGE_CHECK = "/ACS4"
    AGE_CHECK_REGISTRATION = "/api/v4p/acs"
    SPOT = "/SP4"
    CALL = "/V4"
    EXTERNAL_INTERLOCK = "/EIS4"
    TYPING = "/TS"
    CONN_INFO = "/R2"
    HTTP_PROXY = ""
    EXTERNAL_PROXY = ""
    PAY = "/PY4"
    AUTH = "/RS4"
    AUTH_REGISTRATION = "/api/v4p/rs"
    SEARCH = "/search/v1"
    BEACON = "/BEACON4"
    PERSONA = "/PS4"
    SQUARE = "/SQS1"
    POINT = "/POINT4"
    COIN = "/COIN4"
    BAN = "/BAN4"
    BAN_REGISTRATION = "/api/v4p/ban"