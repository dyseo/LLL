import os
from LLL import LLL

USER_ID = os.environ["USER_ID"]
PASSWORD = os.environ["PASSWORD"]

cl = LLL()
cl.setup_by_normal_login(USER_ID, PASSWORD)
# print(cl.client.getProfile())
print(cl.client.getGroupIdsJoined())
