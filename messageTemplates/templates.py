from messageTemplates.notificationTraffic import notificationMessageTraffic
from messageTemplates.notificationKasko import notificationMessageKasko

templates = {
    "traffic": notificationMessageTraffic,
    "kasko": notificationMessageKasko,
}

def getNotificationMessage(data: dict):
    return templates[data['type']](data)