from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

FN = browser.find_element(By.NAME, "firstname")
FN.send_keys("Александр")

LN = browser.find_element(By.NAME, "lastname")
LN.send_keys("Гусев")

EM = browser.find_element(By.NAME, "email")
EM.send_keys("qwe@gmail.com")

btn = browser.find_element(By.CSS_SELECTOR, "#file")

current_dir = os.path.abspath(os.path.dirname(__l2.2s8__))
file_path = os.path.join(current_dir, 'file.txt')

btn.send_keys(file_path)