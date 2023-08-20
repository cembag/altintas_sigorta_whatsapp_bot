from firebaseConfig import firestore
from firebase_admin.firestore import firestore as firestoreTypes
from firebase_admin import firestore as fr
from selenium import webdriver
from whatsapp import WhatsappBot
from messageTemplates.templates import getNotificationMessage
from notificationService import NotificationService
from typing import List
import threading
import time

callback_done = threading.Event()
driver = webdriver.Chrome()
wpBot = WhatsappBot(driver=driver)
notificationService = NotificationService(driver=driver, whatsappBot=wpBot)

def start():
    driver.implicitly_wait(10)
    driver.get("https://web.whatsapp.com")
    wpBot.waitPageLoad()

    messages_ref = firestore.collection('notifications')
    messages_watch = messages_ref.where(filter=firestoreTypes.FieldFilter("should_send_message", "==", True)).on_snapshot(messages_on_snapshot)
    time.sleep(2000)

def messages_on_snapshot(col_snapshot: List[firestoreTypes.DocumentSnapshot], changes, read_time):
    for doc in col_snapshot:
        notification = doc.to_dict()
        notificationId = doc.id
        notification.update({"id": notificationId})
        notificationService.sendMessage(notification)
    callback_done.set()

start()




