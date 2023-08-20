from firebaseConfig import firestore, database
from messageTemplates.templates import getNotificationMessage
from selenium.webdriver.chrome import webdriver
from whatsapp import WhatsappBot
from firebase_admin import firestore as fr
from datetime import datetime

class NotificationService:
    def __init__(self, driver: webdriver.WebDriver, whatsappBot: WhatsappBot):
        self.driver = driver
        self.whatsappBot = whatsappBot

    def sendMessage(self, notification: dict):
        canSendMessage = self.__canSendNotificationMessage(notification)
        if canSendMessage:
            message = getNotificationMessage(notification)
            isSent = self.whatsappBot.sendMessageFromUrl(phone=notification['phone'], message=message)
            if isSent:
                self.__updateFirestore(policyId=notification['id'], policyType=notification['type'],userId=notification['user_id'], phone=notification['phone'], message=message)

    def __updateFirestore(self, policyId, policyType, userId, phone, message):
        
        firestore.collection('notifications').document(policyId).update({
            "should_send_message": False,
            "last_sent_at": datetime.utcnow(),
            "has_message_sent_before": True,
            "message_sent_times": fr.firestore.Increment(1)
        })
        
        firestore.collection('notificationHistory').add({
            "policy_id": policyId,
            "policy_type": policyType,
            "created_at": datetime.utcnow(),
            "message": message,
            "user_id": userId,
            "phone": phone
        })

    def __canSendNotificationMessage(self, data: dict) -> bool:
        policyId = data['id']
        userId = data['user_id']
        phone = data['phone']

        privileges = firestore.collection('privileges').document(userId).get()
        # offers = firestore.collection('policies').document(policyId).collection('offers').where(fr.firestore.FieldFilter('is_active', '==', True)).get()

        # if len(offers) == 0:
        #     return False

        if privileges.exists:
            privileges = privileges.to_dict()
            if not privileges['auto_message']:
                return False
        else:
            return False
       
        if not data['should_send_message'] and not data['status'] == "continue":
            return False

        data = database.reference('blacklist').get()
        blacklist = list(data.values())

        if userId in blacklist or phone in blacklist:
            return False
            
        return True