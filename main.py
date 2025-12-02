import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service(r"C:\Users\arpan\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.get('https://rahulshettyacademy.com/client/#/auth/register')
driver.maximize_window()

driver.find_element(By.ID,'firstName').send_keys('Arpan Kumar')
driver.find_element(By.ID,'lastName').send_keys('Das')
driver.find_element(By.XPATH,'//input[@formcontrolname="userEmail"]').send_keys('arpan98test@gmail.com')
driver.find_element(By.XPATH, '//input[@formcontrolname="userMobile"]').send_keys('6766776787')
driver.find_element(By.XPATH,'//select[@formcontrolname="occupation"]/option[3]').click()
driver.find_element(By.XPATH,'//input[@value="Male"]').click()
driver.find_element(By.ID, 'userPassword').send_keys('Arpan45$@12')
driver.find_element(By.ID, 'confirmPassword').send_keys('Arpan45$@12')
driver.find_element(By.XPATH, '//input[@type="checkbox"]').click()
driver.find_element(By.CSS_SELECTOR, '#login').click()

time.sleep(8)


