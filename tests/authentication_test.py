from LLL.LCL import lll_client

#USER_ID = os.environ["USER_ID"]
#PASSWORD = os.environ["PASSWORD"]

l = lll_client()
l.getProfile()


group_ids = l.getGroupIdsJoined()

for gid in group_ids:
  g = l.getGroup(gid)
  print("Group name -> %s", g.name)
  print("Group id -> %s", gid)
  # print("Group invitation url -> %s", l.reissueGroupTicket(gid))
