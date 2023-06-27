from selenium import webdriver
from selenium.webdriver.common.by import By
import time

controller = webdriver.Chrome()

controller.get("https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F")

#Get an element by ID
email = controller.find_element(By.ID,'form-group--1')
password = controller.find_element(By.ID,'form-group--3')

#Send data to the selected elements, it simulates a user typing
email.send_keys('dahima9413@dotvilla.com')
password.send_keys('Contra123')
time.sleep(2)
submit = controller.find_element(By.LINK_TEXT, 'Iniciar sesión')
submit.click()
time.sleep(8)
#Dispose a controller
controller.quit()