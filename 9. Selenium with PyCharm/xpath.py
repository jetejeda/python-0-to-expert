from selenium import webdriver
from selenium.webdriver.common.by import By
import time

controller = webdriver.Chrome()


controller.get("https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F")
controller.maximize_window()

#Get html tag with a rel XPath
email = controller.find_element(By.XPATH, "//input[@id='form-group--1']")
password = controller.find_element(By.XPATH, "//input[@id='form-group--3']")

#Get html tag with a abs XPath
submit = controller.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/form[1]/button[1]")

#Send data to the selected elements, it simulates a user typing
email.send_keys('dahima9413@dotvilla.com')
password.send_keys('YourPassword')
time.sleep(2)
submit.click()
time.sleep(12)