
from selenium import webdriver
from time import sleep
browser = webdriver.Chrome()
print(browser.capabilities)
print(dir(browser))
browser.get("https://www.stepstone.de/")
current_url=browser.current_url
print(browser.current_url)
if (current_url=="https://www.stepstone.de/"):
    print("test case pass")
else:
    print("test failed")
sleep(15)
browser.close()