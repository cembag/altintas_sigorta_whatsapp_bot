from selenium.webdriver.common.by import By

elements = {
    "chatScroll": {
        "by": By.XPATH,
        "value": '//*[@id="pane-side"]',
    },
    "messageInput": {
        "by": By.XPATH,
        "value": '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[1]/div[1]'
    },
    "status": {
        "by": By.XPATH,
        "value": '//*[@id="main"]/header/div[2]/div[2]/span'
    },
    "searchInput": {
        "by": By.XPATH,
        "value": '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]'
    },
    "sendButton": {
        "by": By.XPATH,
        "value": '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button'
    },
    "searchResults": {
        "by": By.XPATH,
        "value": '//*[@id="pane-side"]/div[1]/div/div',
    }
}
