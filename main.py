#Импортирование библиотек
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#options.add_argument("--headless") #Headless режим
base_url = 'https://www.saucedemo.com/' #Базовый URL
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

#Открыть окно браузера
driver.get(base_url)
driver.set_window_size(1920, 1080)
print('Открыто окно браузера')

#Ввести неправильный логин
user_name = driver.find_element(By.XPATH, "//input[@id = 'user-name']")
user_name.send_keys('standard_us')
print('Введен неправильный логин')

#Ввести неправильный пароль
password = driver.find_element(By.XPATH, "//input[@id = 'password']")
password.send_keys('secret_s')
print('Введен неправильный пароль')

#Выделение полей и удаление
user_name.send_keys(Keys.CONTROL + 'a')
user_name.send_keys(Keys.DELETE)
password.send_keys(Keys.CONTROL + 'a')
password.send_keys(Keys.DELETE)
print('Поля очищены')

#Ввод правильных данных
user_name.send_keys('standard_user')
password.send_keys('secret_sauce')
print('Введены правильные данные')

#Нажатие на кнопку авторизации
button_click = driver.find_element(By.XPATH, "//input[@id = 'login-button']")
button_click.click()
print('Нажата кнопка авторизации')



