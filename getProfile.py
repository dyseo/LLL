from LLL.client import LineClient

cli = LineClient()
#cli.qr_login()
cli.email_login("youremail@gmail.com", "yourpassword")


print(cli.client.getProfile())