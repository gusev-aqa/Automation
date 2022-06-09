from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

prc = WebDriverWait(browser, 10).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
btn = browser.find_element(By.ID, "book").click()

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

elm_x = browser.find_element(By.ID, "input_value")
x = elm_x.text
y = calc(x)

ans = browser.find_element(By.ID, "answer")
ans.send_keys(y)

sbmt = browser.find_element(By.ID,"solve").click()

time.sleep(5)
browser.quit()