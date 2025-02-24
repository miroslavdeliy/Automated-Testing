#Импорт необходимых библиотек
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

#Открытие окна браузера
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.set_window_size(1920,1080)

#Ввод логина
user_name = driver.find_element(By.ID, 'user-name')
user_name.send_keys("standard_user")
print('Введен логин')

#Вод пароля
password = driver.find_element(By.ID, 'password')
password.send_keys("secret_sauce")
print('Введен пароль')

#Нажатие на кнопку авторизации
button_login = driver.find_element(By.ID, 'login-button')
button_login.click()
print('Нажата кнопка авторизации')

#Отправление товара в корзину и переход в нее
button_add_backpack = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
button_cart_link = driver.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']").click()

time.sleep(1)

#Перейти на страницу каталога назад
driver.back()
print("Вернулись назад")

time.sleep(1)

#Перейти на страницу вперед в корзину
driver.forward()
print("Перешли вперед")