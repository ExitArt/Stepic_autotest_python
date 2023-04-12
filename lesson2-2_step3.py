from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, "num1").text
    y = browser.find_element(By.ID, "num2").text
    print(x, y)
    def calc(sum):
        return str(int(x) + int(y))
    s = calc(sum)
    print(s)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(s)
    button1 = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button1.click()

finally:
    time.sleep(5)
    browser.quit()