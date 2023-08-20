from dateService import DateService
from firebaseConfig import firestore

def notificationMessageTraffic(data: dict) -> str:
    policy = firestore.collection('policies').document(data['id']).get().to_dict()

    LICENSE_PLATE = policy['license_plate'].upper()
    EXPIRED_AT = data['expired_at']

    dateService = DateService()
    diffByHours = dateService.getDiffFirebaseDateFromNowByHours(EXPIRED_AT)
    diffByDays = diffByHours / 24

    if diffByHours > 24:
        MESSAGE_TEMPLATE = "{license_plate} plakalı aracınızın sigortası " + str(diffByDays) + " gün sonra bitecektir." 
    elif abs(diffByHours) <= 24:
        print(abs(diffByHours))
        MESSAGE_TEMPLATE = "{license_plate} plakalı aracınızın sigortası bugün itibariyle bitiyor."
    else:
        MESSAGE_TEMPLATE = "{license_plate} plakalı aracınızın sigortası " + str(diffByDays) + " gün önce bitmiştir." 

    MESSAGE = MESSAGE_TEMPLATE.format(license_plate=LICENSE_PLATE)
    return MESSAGE