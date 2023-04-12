from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)
    button1 = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button1.click()
    alert = browser.switch_to.alert
    alert.accept()
    x = browser.find_element(By.ID, "input_value").text
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    button2 = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button2.click()

finally:
    time.sleep(5)
    browser.quit()