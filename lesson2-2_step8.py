from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Иванов")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Иван")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("Иванович")
    element = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element.send_keys(file_path)
    button1 = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button1.click()

finally:
    time.sleep(5)
    browser.quit()