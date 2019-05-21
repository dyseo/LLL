from .LLL_core import LLL_core
from .legy_types import LEGY_ENDPOINT

class lll_client(LLL_core):
  
  def getProfile(self):
    return self.client.getProfile()

  def getLastOpRevision(self):
    return self.client.getLastOpRevision()

  def fetchOperations(self, localRev, count):
    self.set_endpoint(LEGY_ENDPOINT.LONG_POLLING)
    ret = self.client.fetchOperations(localRev, count)
    self.set_endpoint(LEGY_ENDPOINT.NORMAL)
    return ret
