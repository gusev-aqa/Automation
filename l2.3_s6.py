from gettext import find
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

btn = browser.find_element(By.CSS_SELECTOR, ".trollface.btn").click()
time.sleep(1)

sec_win = browser.window_handles[1]
browser.switch_to.window(sec_win)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

elm_x = browser.find_element(By.ID, "input_value")
x = elm_x.text
y = calc(x)

inp = browser.find_element(By.ID, "answer")
inp.send_keys(y)

sbmt = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

time.sleep(5)
browser.quit()