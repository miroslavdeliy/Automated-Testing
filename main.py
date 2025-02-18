#Импортирование библиотек
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#options.add_argument("--headless") #Headless режим
base_url = 'https://www.saucedemo.com/' #Базовый URL
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

#Открыть окно браузера
driver.get(base_url)
driver.set_window_size(1920, 1080)

#Ввести неверный логин
user_name = driver.find_element(By.XPATH, "//input[@id = 'user-name']")
user_name.send_keys('standard_user')
print('Введен логин')

#Ввести пароль
password = driver.find_element(By.XPATH, "//input[@id = 'password']")
password.send_keys('secret_sauce')
print('Введен пароль')

#Выделение полей логина и пароля и удаление их
user_name.send_keys(Keys.CONTROL + 'a')
time.sleep(2)
user_name.send_keys(Keys.BACKSPACE)
password.send_keys(Keys.CONTROL + 'a')
time.sleep(2)
password.send_keys(Keys.BACKSPACE)

#Нажатие на кнопку авторизации
button_click = driver.find_element(By.XPATH, "//input[@id = 'login-button']")
button_click.click()


