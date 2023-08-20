from messageTemplates.messageTemplate import MessageTemplate

class KaskoTemplate(MessageTemplate):

    def template(self, data: dict) -> str:
        print(data)
        return data['brand']