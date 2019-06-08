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

  def sendMessage(self, seq, message):
    return self.client.sendMessage(seq, message)
  
  def acceptGroupInvitation(self, reqSeq, groupId):
    """
    Parameters:
     - reqSeq
     - groupId
    """
    return self.client.acceptGroupInvitation(reqSeq, groupId)

  def acceptGroupInvitationByTicket(self, reqSeq, groupId, ticketId):
    """
    Parameters:
     - reqSeq
     - groupId
     - ticketId
    """
    return self.client.acceptGroupInvitationByTicket(reqSeq, groupID, ticketId)

  def acceptProximityMatches(self, sessionId, ids):
    """
    Parameters:
     - sessionId
     - ids
    """
    pass

  def acquireCallRoute(self, to):
    """
    Parameters:
     - to
    """
    pass

  def acquireCallTicket(self, to):
    """
    Parameters:
     - to
    """
    pass

  def acquireEncryptedAccessToken(self, featureType):
    """
    Parameters:
     - featureType
    """
    pass

  def acquireGroupCallRoute(self, to):
     """
     Parameters:
     - to
     """

  def addSnsId(self, snsIdType, snsAccessToken):
    """
    Parameters:
     - snsIdType
     - snsAccessToken
    """
    pass

  def blockContact(self, reqSeq, id):
    """
    Parameters:
     - reqSeq
     - id
    """
    pass

  def blockRecommendation(self, reqSeq, id):
    """
    Parameters:
     - reqSeq
     - id
    """
    pass

  def cancelGroupInvitation(self, reqSeq, groupId, contactIds):
    """
    Parameters:
     - reqSeq
     - groupId
     - contactIds
    """
    pass

  def changeVerificationMethod(self, sessionId, method):
    """
    Parameters:
     - sessionId
     - method
    """
    pass

  def clearIdentityCredential(self):
    pass

  def clearMessageBox(self, channelId, messageBoxId):
    """
    Parameters:
     - channelId
     - messageBoxId
    """
    pass

  def closeProximityMatch(self, sessionId):
    """
    Parameters:
     - sessionId
    """
    pass

  def commitSendMessage(self, seq, messageId, receiverMids):
    """
    Parameters:
     - seq
     - messageId
     - receiverMids
    """
    pass

  def commitSendMessages(self, seq, messageIds, receiverMids):
    """
    Parameters:
     - seq
     - messageIds
     - receiverMids
    """
    pass

  def commitUpdateProfile(self, seq, attrs, receiverMids):
    """
    Parameters:
     - seq
     - attrs
     - receiverMids
    """
    pass

  def confirmEmail(self, verifier, pinCode):
    """
    Parameters:
     - verifier
     - pinCode
    """
    pass

  def createGroup(self, seq, name, contactIds):
    """
    Parameters:
     - seq
     - name
     - contactIds
    """
    pass

  def createQrcodeBase64Image(self, url, characterSet, imageSize, x, y, width, height):
    """
    Parameters:
     - url
     - characterSet
     - imageSize
     - x
     - y
     - width
     - height
    """
    pass

  def createRoom(self, reqSeq, contactIds):
    """
    Parameters:
     - reqSeq
     - contactIds
    """
    pass

  def createSession(self):
    pass

  def fetchAnnouncements(self, lastFetchedIndex):
    """
    Parameters:
     - lastFetchedIndex
    """
    pass

  def fetchMessages(self, localTs, count):
    """
    Parameters:
     - localTs
     - count
    """
    pass

  def fetchOperations(self, localRev, count):
    """
    Parameters:
     - localRev
     - count
    """
    pass

  def fetchOps(self, localRev, count, globalRev, individualRev):
    """
    Parameters:
     - localRev
     - count
     - globalRev
     - individualRev
    """
    pass

  def findAndAddContactsByEmail(self, reqSeq, emails):
    """
    Parameters:
     - reqSeq
     - emails
    """
    pass

  def findAndAddContactsByMid(self, reqSeq, mid):
    """
    Parameters:
     - reqSeq
     - mid
    """
    pass

  def findAndAddContactsByPhone(self, reqSeq, phones):
    """
    Parameters:
     - reqSeq
     - phones
    """
    pass

  def findAndAddContactsByUserid(self, reqSeq, userid):
    """
    Parameters:
     - reqSeq
     - userid
    """
    pass

  def findContactByUserid(self, userid):
    """
    Parameters:
     - userid
    """
    pass

  def findContactByUserTicket(self, ticketId):
    """
    Parameters:
     - ticketId
    """
    pass

  def findGroupByTicket(self, ticketId):
    """
    Parameters:
     - ticketId
    """
    pass

  def findContactsByEmail(self, emails):
    """
    Parameters:
     - emails
    """
    pass

  def findContactsByPhone(self, phones):
    """
    Parameters:
     - phones
    """
    pass

  def findSnsIdUserStatus(self, snsIdType, snsAccessToken, udidHash):
    """
    Parameters:
     - snsIdType
     - snsAccessToken
     - udidHash
    """
    pass

  def finishUpdateVerification(self, sessionId):
    """
    Parameters:
     - sessionId
    """
    pass

  def generateUserTicket(self, expirationTime, maxUseCount):
    """
    Parameters:
     - expirationTime
     - maxUseCount
    """
    pass

  def getAcceptedProximityMatches(self, sessionId):
    """
    Parameters:
     - sessionId
    """
    pass

  def getActiveBuddySubscriberIds(self):
    pass

  def getAllContactIds(self):
    pass

  def getAuthQrcode(self, keepLoggedIn, systemName):
    """
    Parameters:
     - keepLoggedIn
     - systemName
    """
    pass

  def getBlockedContactIds(self):
    pass

  def getBlockedContactIdsByRange(self, start, count):
    """
    Parameters:
     - start
     - count
    """
    pass

  def getBlockedRecommendationIds(self):
    pass

  def getBuddyBlockerIds(self):
    pass

  def getBuddyLocation(self, mid, index):
    """
    Parameters:
     - mid
     - index
    """
    pass

  def getCompactContactsModifiedSince(self, timestamp):
    """
    Parameters:
     - timestamp
    """
    pass

  def getCompactGroup(self, groupId):
    """
    Parameters:
     - groupId
    """
    pass

  def getCompactRoom(self, roomId):
    """
    Parameters:
     - roomId
    """
    pass

  def getContact(self, id):
    """
    Parameters:
     - id
    """
    pass

  def getContacts(self, ids):
    """
    Parameters:
     - ids
    """
    pass

  def getCountryWithRequestIp(self):
    pass

  def getFavoriteMids(self):
    pass

  def getGroup(self, groupId):
    """
    Parameters:
     - groupId
    """
    self.client.getGroup(groupId)

  def getGroupIdsInvited(self):
    pass

  def getGroupIdsJoined(self):
    self.client.getGroupIdsJoined()

  def getGroups(self, groupIds):
    """
    Parameters:
     - groupIds
    """
    pass

  def getHiddenContactMids(self):
    pass

  def getIdentityIdentifier(self):
    pass

  def getLastAnnouncementIndex(self):
    pass

  def getLastOpRevision(self):
    pass

  def getMessageBox(self, channelId, messageBoxId, lastMessagesCount):
    """
    Parameters:
     - channelId
     - messageBoxId
     - lastMessagesCount
    """
    pass

  def getMessageBoxCompactWrapUp(self, mid):
    """
    Parameters:
     - mid
    """
    pass

  def getMessageBoxCompactWrapUpList(self, start, messageBoxCount):
    """
    Parameters:
     - start
     - messageBoxCount
    """
    pass

  def getMessageBoxList(self, channelId, lastMessagesCount):
    """
    Parameters:
     - channelId
     - lastMessagesCount
    """
    pass

  def getMessageBoxListByStatus(self, channelId, lastMessagesCount, status):
    """
    Parameters:
     - channelId
     - lastMessagesCount
     - status
    """
    pass

  def getMessageBoxWrapUp(self, mid):
    """
    Parameters:
     - mid
    """
    pass

  def getMessageBoxWrapUpList(self, start, messageBoxCount):
    """
    Parameters:
     - start
     - messageBoxCount
    """
    pass

  def getMessagesBySequenceNumber(self, channelId, messageBoxId, startSeq, endSeq):
    """
    Parameters:
     - channelId
     - messageBoxId
     - startSeq
     - endSeq
    """
    pass

  def getNextMessages(self, messageBoxId, startSeq, messagesCount):
    """
    Parameters:
     - messageBoxId
     - startSeq
     - messagesCount
    """
    pass

  def getNotificationPolicy(self, carrier):
    """
    Parameters:
     - carrier
    """
    pass

  def getPreviousMessages(self, messageBoxId, endSeq, messagesCount):
    """
    Parameters:
     - messageBoxId
     - endSeq
     - messagesCount
    """
    pass

  def getProfile(self):
    pass

  def getProximityMatchCandidateList(self, sessionId):
    """
    Parameters:
     - sessionId
    """
    pass

  def getProximityMatchCandidates(self, sessionId):
    """
    Parameters:
     - sessionId
    """
    pass

  def getRecentMessages(self, messageBoxId, messagesCount):
    """
    Parameters:
     - messageBoxId
     - messagesCount
    """
    pass

  def getRecommendationIds(self):
    pass

  def getRoom(self, roomId):
    """
    Parameters:
     - roomId
    """
    pass

  def getRSAKeyInfo(self, provider):
    """
    Parameters:
     - provider
    """
    pass

  def getServerTime(self):
    pass

  def getSessions(self):
    pass

  def getSettings(self):
    pass

  def getSettingsAttributes(self, attrBitset):
    """
    Parameters:
     - attrBitset
    """
    pass

  def getSystemConfiguration(self):
    pass

  def getUserTicket(self):
    pass

  def getWapInvitation(self, invitationHash):
    """
    Parameters:
     - invitationHash
    """
    pass

  def invalidateUserTicket(self):
    pass

  def inviteFriendsBySms(self, phoneNumberList):
    """
    Parameters:
     - phoneNumberList
    """
    pass

  def inviteIntoGroup(self, reqSeq, groupId, contactIds):
    """
    Parameters:
     - reqSeq
     - groupId
     - contactIds
    """
    pass

  def inviteIntoRoom(self, reqSeq, roomId, contactIds):
    """
    Parameters:
     - reqSeq
     - roomId
     - contactIds
    """
    pass

  def inviteViaEmail(self, reqSeq, email, name):
    """
    Parameters:
     - reqSeq
     - email
     - name
    """
    pass

  def isIdentityIdentifierAvailable(self, provider, identifier):
    """
    Parameters:
     - provider
     - identifier
    """
    pass

  def isUseridAvailable(self, userid):
    """
    Parameters:
     - userid
    """
    pass

  def kickoutFromGroup(self, reqSeq, groupId, contactIds):
    """
    Parameters:
     - reqSeq
     - groupId
     - contactIds
    """
    pass

  def leaveGroup(self, reqSeq, groupId):
    """
    Parameters:
     - reqSeq
     - groupId
    """
    pass

  def leaveRoom(self, reqSeq, roomId):
    """
    Parameters:
     - reqSeq
     - roomId
    """
    pass

  def loginWithIdentityCredential(self, identityProvider, identifier, password, keepLoggedIn, accessLocation, systemName, certificate):
    """
    Parameters:
     - identityProvider
     - identifier
     - password
     - keepLoggedIn
     - accessLocation
     - systemName
     - certificate
    """
    pass

  def loginWithIdentityCredentialForCertificate(self, identityProvider, identifier, password, keepLoggedIn, accessLocation, systemName, certificate):
    """
    Parameters:
     - identityProvider
     - identifier
     - password
     - keepLoggedIn
     - accessLocation
     - systemName
     - certificate
    """
    pass

  def loginZ(self, identityProvider, identifier, password, keepLoggedIn, accessLocation, systemName, certificate):
    """
    Parameters:
     - identityProvider
     - identifier
     - password
     - keepLoggedIn
     - accessLocation
     - systemName
     - certificate
    """
    pass

  def loginWithVerifier(self, verifier):
    """
    Parameters:
     - verifier
    """
    pass

  def loginWithVerifierForCerificate(self, verifier):
    """
    Parameters:
     - verifier
    """
    pass

  def loginWithVerifierForCertificate(self, verifier):
    """
    Parameters:
     - verifier
    """
    pass

  def logout(self):
    pass

  def logoutSession(self, tokenKey):
    """
    Parameters:
     - tokenKey
    """
    pass

  def noop(self):
    pass

  def notifiedRedirect(self, paramMap):
    """
    Parameters:
     - paramMap
    """
    pass

  def notifyBuddyOnAir(self, seq, receiverMids):
    """
    Parameters:
     - seq
     - receiverMids
    """
    pass

  def notifyIndividualEvent(self, notificationStatus, receiverMids):
    """
    Parameters:
     - notificationStatus
     - receiverMids
    """
    pass

  def notifyInstalled(self, udidHash, applicationTypeWithExtensions):
    """
    Parameters:
     - udidHash
     - applicationTypeWithExtensions
    """
    pass

  def notifyRegistrationComplete(self, udidHash, applicationTypeWithExtensions):
    """
    Parameters:
     - udidHash
     - applicationTypeWithExtensions
    """
    pass

  def notifySleep(self, lastRev, badge):
    """
    Parameters:
     - lastRev
     - badge
    """
    pass

  def notifyUpdated(self, lastRev, deviceInfo):
    """
    Parameters:
     - lastRev
     - deviceInfo
    """
    pass

  def openProximityMatch(self, location):
    """
    Parameters:
     - location
    """
    pass

  def registerBuddyUser(self, buddyId, registrarPassword):
    """
    Parameters:
     - buddyId
     - registrarPassword
    """
    pass

  def registerBuddyUserid(self, seq, userid):
    """
    Parameters:
     - seq
     - userid
    """
    pass

  def registerDevice(self, sessionId):
    """
    Parameters:
     - sessionId
    """
    pass

  def registerDeviceWithIdentityCredential(self, sessionId, provider, identifier, verifier):
    """
    Parameters:
     - sessionId
     - provider
     - identifier
     - verifier
    """
    pass

  def registerDeviceWithoutPhoneNumber(self, region, udidHash, deviceInfo):
    """
    Parameters:
     - region
     - udidHash
     - deviceInfo
    """
    pass

  def registerDeviceWithoutPhoneNumberWithIdentityCredential(self, region, udidHash, deviceInfo, provider, identifier, verifier, mid):
    """
    Parameters:
     - region
     - udidHash
     - deviceInfo
     - provider
     - identifier
     - verifier
     - mid
    """
    pass

  def registerUserid(self, reqSeq, userid):
    """
    Parameters:
     - reqSeq
     - userid
    """
    pass

  def registerWapDevice(self, invitationHash, guidHash, email, deviceInfo):
    """
    Parameters:
     - invitationHash
     - guidHash
     - email
     - deviceInfo
    """
    pass

  def registerWithExistingSnsIdAndIdentityCredential(self, identityCredential, region, udidHash, deviceInfo):
    """
    Parameters:
     - identityCredential
     - region
     - udidHash
     - deviceInfo
    """
    pass

  def registerWithSnsId(self, snsIdType, snsAccessToken, region, udidHash, deviceInfo, mid):
    """
    Parameters:
     - snsIdType
     - snsAccessToken
     - region
     - udidHash
     - deviceInfo
     - mid
    """
    pass

  def registerWithSnsIdAndIdentityCredential(self, snsIdType, snsAccessToken, identityCredential, region, udidHash, deviceInfo):
    """
    Parameters:
     - snsIdType
     - snsAccessToken
     - identityCredential
     - region
     - udidHash
     - deviceInfo
    """
    pass

  def reissueDeviceCredential(self):
    pass

  def reissueUserTicket(self, expirationTime, maxUseCount):
    """
    Parameters:
     - expirationTime
     - maxUseCount
    """
    pass

  def reissueGroupTicket(self, groupId):
    """
    Parameters:
     - groupId
    """
    self.client.reissueGroupTicket(groupId)

  def rejectGroupInvitation(self, reqSeq, groupId):
    """
    Parameters:
     - reqSeq
     - groupId
    """
    pass

  def releaseSession(self):
    pass

  def removeAllMessages(self, seq, lastMessageId):
    """
    Parameters:
     - seq
     - lastMessageId
    """
    pass

  def removeBuddyLocation(self, mid, index):
    """
    Parameters:
     - mid
     - index
    """
    pass

  def removeMessage(self, messageId):
    """
    Parameters:
     - messageId
    """
    pass

  def removeMessageFromMyHome(self, messageId):
    """
    Parameters:
     - messageId
    """
    pass

  def removeSnsId(self, snsIdType):
    """
    Parameters:
     - snsIdType
    """
    pass

  def report(self, syncOpRevision, category, report):
    """
    Parameters:
     - syncOpRevision
     - category
     - report
    """
    pass

  def reportContacts(self, syncOpRevision, category, contactReports, actionType):
    """
    Parameters:
     - syncOpRevision
     - category
     - contactReports
     - actionType
    """
    pass

  def reportGroups(self, syncOpRevision, groups):
    """
    Parameters:
     - syncOpRevision
     - groups
    """
    pass

  def reportProfile(self, syncOpRevision, profile):
    """
    Parameters:
     - syncOpRevision
     - profile
    """
    pass

  def reportRooms(self, syncOpRevision, rooms):
    """
    Parameters:
     - syncOpRevision
     - rooms
    """
    pass

  def reportSettings(self, syncOpRevision, settings):
    """
    Parameters:
     - syncOpRevision
     - settings
    """
    pass

  def reportSpammer(self, spammerMid, spammerReasons, spamMessageIds):
    """
    Parameters:
     - spammerMid
     - spammerReasons
     - spamMessageIds
    """
    pass

  def requestAccountPasswordReset(self, provider, identifier, locale):
    """
    Parameters:
     - provider
     - identifier
     - locale
    """
    pass

  def requestEmailConfirmation(self, emailConfirmation):
    """
    Parameters:
     - emailConfirmation
    """
    pass

  def requestIdentityUnbind(self, provider, identifier):
    """
    Parameters:
     - provider
     - identifier
    """
    pass

  def resendEmailConfirmation(self, verifier):
    """
    Parameters:
     - verifier
    """
    pass

  def resendPinCode(self, sessionId):
    """
    Parameters:
     - sessionId
    """
    pass

  def resendPinCodeBySMS(self, sessionId):
    """
    Parameters:
     - sessionId
    """
    pass

  def sendChatChecked(self, seq, consumer, lastMessageId):
    """
    Parameters:
     - seq
     - consumer
     - lastMessageId
    """
    pass

  def sendChatRemoved(self, seq, consumer, lastMessageId):
    """
    Parameters:
     - seq
     - consumer
     - lastMessageId
    """
    pass

  def sendContentPreviewUpdated(self, esq, messageId, receiverMids):
    """
    Parameters:
     - esq
     - messageId
     - receiverMids
    """
    pass

  def sendContentReceipt(self, seq, consumer, messageId):
    """
    Parameters:
     - seq
     - consumer
     - messageId
    """
    pass

  def sendDummyPush(self):
    pass

  def sendEvent(self, seq, message):
    """
    Parameters:
     - seq
     - message
    """
    pass

  def sendMessage(self, seq, message):
    """
    Parameters:
     - seq
     - message
    """
    pass

  def sendMessageIgnored(self, seq, consumer, messageIds):
    """
    Parameters:
     - seq
     - consumer
     - messageIds
    """
    pass

  def sendMessageReceipt(self, seq, consumer, messageIds):
    """
    Parameters:
     - seq
     - consumer
     - messageIds
    """
    pass

  def sendMessageToMyHome(self, seq, message):
    """
    Parameters:
     - seq
     - message
    """
    pass

  def setBuddyLocation(self, mid, index, location):
    """
    Parameters:
     - mid
     - index
     - location
    """
    pass

  def setIdentityCredential(self, provider, identifier, verifier):
    """
    Parameters:
     - provider
     - identifier
     - verifier
    """
    pass

  def setNotificationsEnabled(self, reqSeq, type, target, enablement):
    """
    Parameters:
     - reqSeq
     - type
     - target
     - enablement
    """
    pass

  def startUpdateVerification(self, region, carrier, phone, udidHash, deviceInfo, networkCode, locale):
    """
    Parameters:
     - region
     - carrier
     - phone
     - udidHash
     - deviceInfo
     - networkCode
     - locale
    """
    pass

  def startVerification(self, region, carrier, phone, udidHash, deviceInfo, networkCode, mid, locale):
    """
    Parameters:
     - region
     - carrier
     - phone
     - udidHash
     - deviceInfo
     - networkCode
     - mid
     - locale
    """
    pass

  def storeUpdateProfileAttribute(self, seq, profileAttribute, value):
    """
    Parameters:
     - seq
     - profileAttribute
     - value
    """
    pass

  def syncContactBySnsIds(self, reqSeq, modifications):
    """
    Parameters:
     - reqSeq
     - modifications
    """
    pass

  def syncContacts(self, reqSeq, localContacts):
    """
    Parameters:
     - reqSeq
     - localContacts
    """
    pass

  def trySendMessage(self, seq, message):
    """
    Parameters:
     - seq
     - message
    """
    pass

  def unblockContact(self, reqSeq, id):
    """
    Parameters:
     - reqSeq
     - id
    """
    pass

  def unblockRecommendation(self, reqSeq, id):
    """
    Parameters:
     - reqSeq
     - id
    """
    pass

  def unregisterUserAndDevice(self):
    pass

  def updateApnsDeviceToken(self, apnsDeviceToken):
    """
    Parameters:
     - apnsDeviceToken
    """
    pass

  def updateBuddySetting(self, key, value):
    """
    Parameters:
     - key
     - value
    """
    pass

  def updateC2DMRegistrationId(self, registrationId):
    """
    Parameters:
     - registrationId
    """
    pass

  def updateContactSetting(self, reqSeq, mid, flag, value):
    """
    Parameters:
     - reqSeq
     - mid
     - flag
     - value
    """
    pass

  def updateCustomModeSettings(self, customMode, paramMap):
    """
    Parameters:
     - customMode
     - paramMap
    """
    pass

  def updateDeviceInfo(self, deviceUid, deviceInfo):
    """
    Parameters:
     - deviceUid
     - deviceInfo
    """
    pass

  def updateGroup(self, reqSeq, group):
    """
    Parameters:
     - reqSeq
     - group
    """
    pass

  def updateNotificationToken(self, type, token):
    """
    Parameters:
     - type
     - token
    """
    pass

  def updateNotificationTokenWithBytes(self, type, token):
    """
    Parameters:
     - type
     - token
    """
    pass

  def updateProfile(self, reqSeq, profile):
    """
    Parameters:
     - reqSeq
     - profile
    """
    pass

  def updateProfileAttribute(self, reqSeq, attr, value):
    """
    Parameters:
     - reqSeq
     - attr
     - value
    """
    pass

  def updateRegion(self, region):
    """
    Parameters:
     - region
    """
    pass

  def updateSettings(self, reqSeq, settings):
    """
    Parameters:
     - reqSeq
     - settings
    """
    pass

  def updateSettings2(self, reqSeq, settings):
    """
    Parameters:
     - reqSeq
     - settings
    """
    pass

  def updateSettingsAttribute(self, reqSeq, attr, value):
    """
    Parameters:
     - reqSeq
     - attr
     - value
    """
    pass

  def updateSettingsAttributes(self, reqSeq, attrBitset, settings):
    """
    Parameters:
     - reqSeq
     - attrBitset
     - settings
    """
    pass

  def verifyIdentityCredential(self, identityProvider, identifier, password):
    """
    Parameters:
     - identityProvider
     - identifier
     - password
    """
    pass

  def verifyIdentityCredentialWithResult(self, identityCredential):
    """
    Parameters:
     - identityCredential
    """
    pass

  def verifyPhone(self, sessionId, pinCode, udidHash):
    """
    Parameters:
     - sessionId
     - pinCode
     - udidHash
    """
    pass

  def verifyQrcode(self, verifier, pinCode):
    """
    Parameters:
     - verifier
     - pinCode
    """
    pass

  def fetchMessageOperations(self, localRevision, lastOpTimestamp, count):
    """
    Parameters:
     - localRevision
     - lastOpTimestamp
     - count
    """
    pass

  def getLastReadMessageIds(self, chatId):
    """
    Parameters:
     - chatId
    """
    pass

  def multiGetLastReadMessageIds(self, chatIds):
    """
    Parameters:
     - chatIds
    """
    pass
