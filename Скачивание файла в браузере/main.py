import glob
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
time.sleep(15)

#Проверка, что файл в директории
file_name = "LambdaTest.pdf"
file_path = path_download + file_name
assert os.access(file_path, os.F_OK) == True, 'Ошибка! Файл не в директории!'
print("Файл в директории")

#Проверка, что файл не пустой
files = glob.glob(os.path.join(path_download, "*.*"))
for file in files:
    a = os.path.getsize(file)
    if a > 10:
        print("Файл не пустой")
    else:
        print("Файл пустой")

#Удаляет файл
files = glob.glob(os.path.join(path_download, "*.*"))
for file in files:
    os.remove(file)
print('Файл удален')

