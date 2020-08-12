from selenium import webdriver
from time import sleep
browser = webdriver.Chrome()
browser.get("https://www.stepstone.de/")
current_url=browser.current_url
print(browser.current_url)

jobtitle_box=browser.find_element_by_name("ke")
jobtitle_box.send_keys("lichtplanner")
joblocation_box=browser.find_element_by_name("ws")
joblocation_box.send_keys("Hamburg")
click_button=browser.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[3]/div/div/div/div/form/div[2]/div/button/strong")
click_button.click()
sleep(15)
browser.close()