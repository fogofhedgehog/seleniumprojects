from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    btn = browser.find_element_by_id("book")
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID,"price"), "$100"))
    btn.click()
    vlu = browser.find_element_by_id("input_value")
    x = int(vlu.text)
    y = calc(x)
    answ = browser.find_element_by_id("answer")
    answ.send_keys(str(y))
    btn = browser.find_element_by_id("solve")
    btn.click()

    # Отправляем заполненную форму
#    ppth = os.path.abspath(os.path.dirname(__file__))
#    pth = os.path.join(ppth, '1.py')
#    sndfil = browser.find_element_by_id("file")
#    sndfil.send_keys(pth)

#    btn = browser.find_element_by_css_selector("button.btn")
#    btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(6)
    # закрываем браузер после всех манипуляций
    browser.quit()