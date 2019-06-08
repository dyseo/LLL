from LLL.LCL import lll_client
from LLL.legy_types import * 

class OpType(object):
    END_OF_OPERATION = 0
    UPDATE_PROFILE = 1
    NOTIFIED_UPDATE_PROFILE = 2
    REGISTER_USERID = 3
    ADD_CONTACT = 4
    NOTIFIED_ADD_CONTACT = 5
    BLOCK_CONTACT = 6
    UNBLOCK_CONTACT = 7
    NOTIFIED_RECOMMEND_CONTACT = 8
    CREATE_GROUP = 9
    UPDATE_GROUP = 10
    NOTIFIED_UPDATE_GROUP = 11
    INVITE_INTO_GROUP = 12
    NOTIFIED_INVITE_INTO_GROUP = 13
    LEAVE_GROUP = 14
    NOTIFIED_LEAVE_GROUP = 15
    ACCEPT_GROUP_INVITATION = 16
    NOTIFIED_ACCEPT_GROUP_INVITATION = 17
    KICKOUT_FROM_GROUP = 18
    NOTIFIED_KICKOUT_FROM_GROUP = 19
    CREATE_ROOM = 20
    INVITE_INTO_ROOM = 21
    NOTIFIED_INVITE_INTO_ROOM = 22
    LEAVE_ROOM = 23
    NOTIFIED_LEAVE_ROOM = 24
    SEND_MESSAGE = 25
    RECEIVE_MESSAGE = 26
    SEND_MESSAGE_RECEIPT = 27
    RECEIVE_MESSAGE_RECEIPT = 28
    SEND_CONTENT_RECEIPT = 29
    RECEIVE_ANNOUNCEMENT = 30
    CANCEL_INVITATION_GROUP = 31
    NOTIFIED_CANCEL_INVITATION_GROUP = 32
    NOTIFIED_UNREGISTER_USER = 33
    REJECT_GROUP_INVITATION = 34
    NOTIFIED_REJECT_GROUP_INVITATION = 35
    UPDATE_SETTINGS = 36
    NOTIFIED_REGISTER_USER = 37
    INVITE_VIA_EMAIL = 38
    NOTIFIED_REQUEST_RECOVERY = 39
    SEND_CHAT_CHECKED = 40
    SEND_CHAT_REMOVED = 41
    NOTIFIED_FORCE_SYNC = 42
    SEND_CONTENT = 43
    SEND_MESSAGE_MYHOME = 44
    NOTIFIED_UPDATE_CONTENT_PREVIEW = 45
    REMOVE_ALL_MESSAGES = 46
    NOTIFIED_UPDATE_PURCHASES = 47
    DUMMY = 48
    UPDATE_CONTACT = 49
    NOTIFIED_RECEIVED_CALL = 50
    CANCEL_CALL = 51
    NOTIFIED_REDIRECT = 52
    NOTIFIED_CHANNEL_SYNC = 53
    FAILED_SEND_MESSAGE = 54
    NOTIFIED_READ_MESSAGE = 55
    FAILED_EMAIL_CONFIRMATION = 56
    NOTIFIED_CHAT_CONTENT = 58
    NOTIFIED_PUSH_NOTICENTER_ITEM = 59

l = lll_client()

op = None
rev = l.getLastOpRevision()

while True:
  
  op = l.fetchOperations(rev, 1)[0]
  rev = max(op.revision, rev)

  if op.type == OpType.RECEIVE_MESSAGE:
    m = op.message
    m.to = m.from_

    l.sendMessage(0, m)

