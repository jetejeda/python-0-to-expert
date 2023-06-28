from selenium import webdriver

#Open a Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()

#Enter the url that you want to execute
driver.get("https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F")

driver.close()