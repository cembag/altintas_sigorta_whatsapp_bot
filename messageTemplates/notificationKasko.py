from dateService import DateService
from firebaseConfig import firestore

def notificationMessageKasko(data: dict) -> str:
    policy = firestore.collection('policies').document(data['id']).get().to_dict()

    LICENSE_PLATE = policy['license_plate'].upper()
    EXPIRED_AT = data['expired_at']

    dateService = DateService()
    diffByHours = dateService.getDiffFirebaseDateFromNowByHours(EXPIRED_AT)
    diffByDays = diffByHours / 24

    if diffByHours > 24:
        MESSAGE_TEMPLATE = "selam kardes {license_plate} plakalı aracınızın kasko sigortası" + str(diffByDays) + "gün sonra bitiore \n ona göre yane"
    elif abs(diffByHours) <= 24:
        MESSAGE_TEMPLATE = "selam kardes {license_plate} plakalı aracınızın kasko sigortası bugün bitiore \n ona göre yane"
    else:
        MESSAGE_TEMPLATE = "selam kardes {license_plate} plakalı aracınızın kasko sigortası bittike \n ona göre yane"

    MESSAGE = MESSAGE_TEMPLATE.format(license_plate=LICENSE_PLATE)
    return MESSAGE