#pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from os import getcwd
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_argument("--headless=new")
driver = webdriver.Chrome(options=chrome_options)
website = f"{getcwd()}\\data\\voice.html"

driver.get(website)


def Listen():
    print("LISTENING ... ")
    driver.get(website)
    driver.find_element(by=By.ID, value='start').click()
    while 1:
        text=driver.find_element(by=By.ID, value='output').text
        if text != "":
            print("you said : " + text)
            driver.find_element(by=By.ID, value='end').click()
            return text
if __name__=="__main__":
    while 1:
        Listen()