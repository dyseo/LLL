from LLL.client import LineClient

cli = LineClient()
cli.qr_login()

print(cli.client.getProfile())
