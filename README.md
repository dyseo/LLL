# LLL makes your LINE great again in an unofficial way

#### DISCLAIMER
LLL is currently only compatible to logging in through QR authentication so in case if you'd like email login, please notice that part of code is still WIP. 

#### Example

```
from LLL.LCL import lll_client

l = lll_client() # now you can see a qr code in terminal

l.getProfile()
```

##### TODO
- Polling API
- Add more thrift functions 
- authtoken login
