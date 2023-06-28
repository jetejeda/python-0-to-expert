from selenium import webdriver
from selenium.webdriver.common.by import By
import time

controller = webdriver.Chrome()


controller.get("https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F")
controller.maximize_window()

#Get all the elements that match an specific criteria

elements = controller.find_elements(By.CLASS_NAME, 'ud-compact-form-control')

print(type(elements))

for i in elements:
    i.send_keys('Text sent to many elements')
    time.sleep(2)
#Get html tag with a abs XPath
submit = controller.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/form[1]/button[1]")
submit.click()
time.sleep(12)