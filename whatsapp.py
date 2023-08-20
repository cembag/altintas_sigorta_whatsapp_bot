from elements import elements
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time
# from repeatedTimer import RepeatedTimer

class WhatsappBot:
    def __init__(self, driver: webdriver.WebDriver):
        self.driver = driver

    def sendMessage(self, phone: str, message: str) -> bool:
        actions = ActionChains(self.driver)
        
        # search contact
        search = elements['searchInput']
        searchElement = self.driver.find_element(by=search['by'], value=search['value'])
        searchElement.click()
        self.__clearFields(searchElement)
        searchElement.send_keys(phone)
        time.sleep(.5)
        
        # click contact 
        actions.move_by_offset(40, 210).click().perform()
        actions.reset_actions()
        time.sleep(.5)
        
        # add message to message input
        messageInput = elements['messageInput']
        messageInputElement = self.driver.find_element(by=messageInput['by'], value=messageInput['value'])
        self.__clearFields(messageInputElement)
        messageInputElement.send_keys(message)
        time.sleep(.5)

        # click send button
        sendButton = elements['sendButton']
        sendButtonElement = self.driver.find_element(by=sendButton['by'], value=sendButton['value'])
        sendButtonElement.click()
        return True
    
    def sendMessageFromUrl(self, phone: str, message: str) -> bool:
        CHAT_URL = "https://web.whatsapp.com/send?phone={phone}&text={text}&type=phone_number&app_absent=1"
        url = CHAT_URL.format(phone=phone, text=message)
        self.driver.get(url=url)
        self.waitPageLoad()
        time.sleep(1)

        # send message
        sendButton = elements['sendButton']
        sendButtonElement = self.driver.find_element(by=sendButton['by'], value=sendButton['value'])
        sendButtonElement.click()

        print("Message sended")
        return True

    def __clearFields(self, element: WebElement):
        while len(element.text) > 0:
            element.send_keys(Keys.BACK_SPACE)

    def waitPageLoad(self):
        while True:
            isLoaded = self.__checkIsLoaded()
            if isLoaded:
                print("Page is loaded")
                return
            print("Page is not loaded")
            time.sleep(1)
    
    def __checkIsLoaded(self) -> bool:
        try:
            self.driver.find_element(by=By.XPATH, value='//*[@id="pane-side"]')
        except NoSuchElementException:
            return False
        return True
