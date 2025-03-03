import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

path_download = "C:\\Users\\miros\\PycharmProjects\\pythonProject2\\files_download\\"

options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : path_download}
options.add_experimental_option('prefs', prefs)
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.lambdatest.com/selenium-playground/download-file-demo'
driver.get(base_url)
driver.set_window_size(1920,1080)

#Клик по кнопке Download File
click_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Download File')]")
click_button.click()
time.sleep(5)

#Проверка, что файл в директории
file_name = "LambdaTest.pdf"
file_path = path_download + file_name
assert os.access(file_path, os.F_OK) is True, 'Ошибка! Файл не в директории!'
print("Файл в директории")

#Проверка, что файл не пустой
file_size = os.path.getsize(file_path)
if file_size > 10:
    print('Файл не пустой')
else:
    print('Ошибка! Файл пустой!')
    os.remove(file_path)