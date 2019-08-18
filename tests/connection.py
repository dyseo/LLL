import thriftpy2
from thriftpy2.http import THttpClient
from thriftpy2.protocol import TCompactProtocol
from thriftpy2.thrift import TClient


line_thrift = thriftpy2.load("line.thrift", module_name="line_thrift")

transport = THttpClient("https://gd2.line.naver.jp:443/S4")
transport.setCustomHeaders({
  "User-Agent" : "Line/7.14.0 iPad5,1 10.2.0",
  "X-Line-Application" : "IOSIPAD\t7.14.0\tiPhone OS\t10.12.0",
  "X-LHM" : "POST",
  "X-lal" : "ja-JP_JP"
})
protocol = TCompactProtocol(transport)
transport.open()
client = TClient(line_thrift.LineService, protocol)

transport.path = "/api/v4/TalkService.do"
qr = client.getAuthQrcode(keepLoggedIn=1, systemName="LLL")
