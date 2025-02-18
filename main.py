#Импортирование библиотек
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import datetime

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#options.add_argument("--headless") #Headless режим
base_url = 'https://www.saucedemo.com/' #Базовый URL
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

#Открыть окно браузера
driver.get(base_url)
driver.set_window_size(1920, 1080)
print('Открыто окно браузера')

#Ввести логин
user_name = driver.find_element(By.XPATH, "//input[@id = 'user-name']")
user_name.send_keys('standard_user')
print('Введен логин')

#Ввести пароль
password = driver.find_element(By.XPATH, "//input[@id = 'password']")
password.send_keys('secret_sauce')
print('Введен пароль')

#Нажатие на кнопку авторизации
button_click = driver.find_element(By.XPATH, "//input[@id = 'login-button']")
button_click.click()
print('Нажата кнопка авторизации')

#Создание скриншота
now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
name_screnshot = 'screenshot' + now_date + '.png'
driver.save_screenshot('C:\\Users\\miros\\PycharmProjects\\Send_key\\screen\\' + name_screnshot)
print('Скриншот сохранен')
