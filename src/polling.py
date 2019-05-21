from legy_types import *
from LLL_core import LLL_core

class polling(object):

  def __init__(self, client):
    
    self.client = client
    self.client.set_endpoint(LEGY_ENDPOINT.LONG_POLLING)
