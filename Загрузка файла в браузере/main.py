from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Открыть браузер и перейти по ссылке
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.lambdatest.com/selenium-playground/upload-file-demo'
driver.get(base_url)
driver.set_window_size(1920,1080)

# Загрузка файла
file_path = "C:\\Users\\miros\\Downloads\\cat.jpg"
upload_file_button = driver.find_element(By.XPATH, '//*[@id="file"]')
upload_file_button.send_keys(file_path)
print('Файл загружен')

# Проверка, что файл загружен по имени файла
file_name = os.path.basename(file_path)
print(file_name)
file_path_uploaded = upload_file_button.get_attribute("value")
file_name_uploaded = os.path.basename(file_path_uploaded)
print(file_name_uploaded)
assert file_name == file_name_uploaded, 'Ошибка! Файл загрузился некорректно!'
print('Файл загрузился корректно')