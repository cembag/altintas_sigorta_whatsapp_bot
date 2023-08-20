from firebaseConfig import database, firestore
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from elements import elements
import requests
import random
import time

with open('messages.txt', 'r', encoding= 'utf-8') as messages:
    messageList = list()
    text = messages.read()
    messageList = text.split('\n')

print(messageList)

def start():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get("https://web.whatsapp.com")
    input('QR kodunu okuttan sonra bir tuşa basıp enterlayın')
    
    scrollPx = 800
    chatScroll = elements["chatScroll"]
    chatScrollElement = driver.find_element(by=chatScroll['by'], value=chatScroll['value'])

    chatListElement = driver.find_element(by=By.XPATH, value='//*[@id="pane-side"]/div[1]/div/div')
    userCount = chatListElement.get_attribute('aria-rowcount')

    loopCount: int = 0
    checkedUserCount: int = 0
    failedCheckCount: int = 0
    succeededCheckCount: int = 0
    checkableUserCount: int = 18

    while True:
        try: 
            for iter in range(1, checkableUserCount):
                isOnline = False
                userChatBubble = driver.find_element(by=By.XPATH, value='//*[@id="pane-side"]/div[1]/div/div/div['+str(iter)+']')
                userChatBubble.click()
                
                userNameElement = driver.find_element(by=By.XPATH, value='//*[@id="pane-side"]/div[1]/div/div/div['+str(iter)+']/div/div/div/div[2]/div[1]/div[1]/span')
                userName = userNameElement.text

                status = elements['status']
                statusElement = driver.find_element(by=status['by'], value=status['value'])

                if(statusElement):
                    succeededCheckCount = succeededCheckCount + 1
                    statusText = statusElement.text
                    if(statusText == "çevrimiçi"):
                        isOnline = True
                else:
                    failedCheckCount = failedCheckCount + 1
                
                if(isOnline):
                    driver.execute_script("alert("+ str(userName)+" çevrimiçi)")
                    print(userName + ' çevrimiçi')
                else:
                    print(userName + ' çevrimdışı')
                
                checkedUserCount = checkedUserCount + 1

            driver.execute_script("const element = arguments[0]; const top = element.scrollTop; const elementScrollHeight = element.scrollHeight; if(top >= elementScrollHeight - 1) {{element.scrollTo(0, 0); alert("+str(checkedUserCount)+")}} else if((top + "+str(scrollPx)+") >= elementScrollHeight) {{element.scrollTo(0, elementScrollHeight)}} else {{element.scrollTo(0, top + " +str(scrollPx)+")}}", chatScrollElement)
            print("SCROLLED")
            time.sleep(.5)

        except Exception as e: 
            print("An error accured: ", e)

start()