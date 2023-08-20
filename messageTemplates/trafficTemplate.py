from messageTemplates.messageTemplate import MessageTemplate
from dateService import DateService

class TrafficTemplate(MessageTemplate):

    def template(self, data: dict) -> str:
        dateService = DateService()
        diff = dateService.getDiffFirebaseDateFromNow(data['expired_at']).seconds
        return "Sayın kardes " + data['license_plate'].upper() + " plakaya sahip aracınızın trafik sigortası dolmak üzeredir ananızı sikeyim " + str(diff)
    
    def __template(self, data) -> str:
        dateService = DateService()
        diff = dateService.getDiffFirebaseDateFromNow(data['expired_at']).hours
        return "Sayın kardes " + data['license_plate'].upper() + " plakaya sahip aracınızın trafik sigortası dolmak üzeredir ananızı sikeyim " + str(diff)
    