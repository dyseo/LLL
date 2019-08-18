# LLL makes your LINE great again in an unofficial way

#### DISCLAIMER
LLL is currently only compatible to logging in through QR authentication so in case if you'd like email login, please notice that part of code is still WIP. 

#### Installation

```
git clone https://github.com/roppinhoppin/LLL
cd LLL
pip install -r requirements.txt
python setup.py install
```

#### Example

```
from LLL.cilent import LineClient

cli = LineClient()
cli.qr_login()
```

##### TODO
- Polling API
- Add more thrift functions 
- authtoken login
