import pyqrcode
import requests
import json
import os

import thriftpy2
from thriftpy2.http import THttpClient
from thriftpy2.protocol import TCompactProtocol
from thriftpy2.thrift import TClient


def print_qr(uri):
    print(pyqrcode.create(uri).terminal('green', 'white', 1))


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

    def qr_login(self):
        self.transport.path = LEGY_ENDPOINT.REGISTRATION
        qrcode = self.client.getAuthQrcode(keepLoggedIn=1, systemName='LLL')
        url = "line://au/q/" + qrcode.verifier
        print_qr(url)

        header = {
            "User-Agent": LEGY_ENDPOINT.UA,
            "X-Line-Application": LEGY_ENDPOINT.LA,
            "x-lal": "ja-US_US",
            "x-lpqs": LEGY_ENDPOINT.REGISTRATION,
            "X-Line-Access": qrcode.verifier
        }

        getAccessKey = json.loads(self._session.get("https://gd2.line.naver.jp/Q", headers=header).text)
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
