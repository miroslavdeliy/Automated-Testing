#Импортирование библиотек
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--headless") #Headless режим
base_url = 'https://www.saucedemo.com/' #Базовый URL
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

#Открыть окно браузера
driver.get(base_url)
driver.set_window_size(1920, 1080)

#Авторизация на сайте
user_name = driver.find_element(By.XPATH, "//*[@id='user-name']")
user_name.send_keys("standard_user")
print('Введен логин')
password = driver.find_element(By.XPATH, "//*[@id='password']")
password.send_keys("secret_sauc")
print('Введен пароль')
button_login = driver.find_element(By.XPATH, "//*[@id='login-button']")
button_login.click()
print('Нажата кнопка входа')

#Проверка корректности сообщения о неправильных входных данных
warning_text = driver.find_element(By.XPATH, "//h3[@data-test='error']")
value_warning_text = warning_text.text
assert value_warning_text == 'Epic sadface: Username and password do not match any user in this service', 'Сообщение некорректно!'
print('Сообщение корректно')

#Закрытие окна сообщения об ошибке
error_button = driver.find_element(By.XPATH, "//button[@class='error-button']")
error_button.click()
print('Закрыто сообщение об ошибке!')