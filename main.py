#Импортирование библиотек
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
base_url = 'https://www.saucedemo.com/' #Базовый URL
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

#Открыть окно браузера
driver.get(base_url)
driver.set_window_size(1920, 1080)

#Авторизация на сайте
user_name = driver.find_element(By.XPATH, "//*[@id='user-name']")
user_name.send_keys("standard_user")
print('Input Login')
password = driver.find_element(By.XPATH, "//*[@id='password']")
password.send_keys("secret_sauce")
print('Input Password')
button_login = driver.find_element(By.XPATH, "//*[@id='login-button']")
button_login.click()
print('Click Login Button')

#Проверка, что после авторизации находимся на целевом url
get_url = driver.current_url
url = 'https://www.saucedemo.com/inventory.html'
assert url == get_url
print('URL корректен')

#Проверка, что находимся на странице каталога
text_products = driver.find_element(By.XPATH, "//span[@class='title']")
value_text_products = text_products.text
assert value_text_products == 'Products'
print('Заголовок корректен')