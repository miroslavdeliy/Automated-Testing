#Импортирование библиотек
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#options.add_argument("--headless") #Headless режим
base_url = 'https://www.saucedemo.com/' #Базовый URL
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

#Открыть окно браузера
driver.get(base_url)
driver.set_window_size(1920, 1080)
print('Открыто окно браузера')

#Ввод данных авторизаци
user_name = driver.find_element(By.XPATH, "//input[@id = 'user-name']")
user_name.send_keys('standard_user')
password = driver.find_element(By.XPATH, "//input[@id = 'password']")
password.send_keys('secret_sauce')
print('Введены данные')

#Нажатие на кнопку авторизации
button_click = driver.find_element(By.XPATH, "//input[@id = 'login-button']")
button_click.click()
print('Нажата кнопка авторизации')

#Открытие меню
menu_button = driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]')
menu_button.click()
print('Открыто меню')
time.sleep(1)

#Разлогирование
logout_button = driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]')
logout_button.click()
print('Разлогирование из системы')

