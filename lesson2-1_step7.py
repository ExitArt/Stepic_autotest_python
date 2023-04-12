from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  link = "http://suninjuly.github.io/get_attribute.html"
  browser = webdriver.Chrome()
  browser.get(link)

  tresure_element = browser.find_element(By.ID, "treasure")
  treasure_attribute = tresure_element.get_attribute("valuex")
  x = treasure_attribute
  y = calc(x)
  input1 = browser.find_element(By.ID, "answer")
  input1.send_keys(y)
  option1 = browser.find_element(By.ID, "robotCheckbox")
  option1.click()
  option2 = browser.find_element(By.ID, "robotsRule")
  option2.click()
  button1 = browser.find_element(By.CLASS_NAME, "btn.btn-default")
  button1.click()

finally:
  time.sleep(10)
  browser.quit()