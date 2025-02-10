#Импортирование вебдрайвера
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install())) #Создание объекта driver для работы с Google Chrome
base_url = 'https://www.saucedemo.com/' #Базовый URL
driver.get(base_url) #Открыть ссылку
driver.set_window_size(1920, 1080) #Установить разрешение окна
user_name = driver.find_element(By.XPATH, "//*[@id='user-name']") #Создание объекта поля ввода логина
user_name.send_keys("standard_user") #Ввести данные в поле логина
print('Input Login') #Вывод информации о вводе логина
password = driver.find_element(By.XPATH, "//*[@id='password']") #Создание объекта поля ввода пароля
password.send_keys("secret_sauce") #ввести данные в поле пароля
print('Input Password') #Вывод информации о вводе пароля
button_login = driver.find_element(By.XPATH, "//*[@id='login-button']") #Создание объекта кнопки входа
button_login.click() #Нажать на кнопку
print('Click Login Button') #Вывод информации о нажатии на кнопку
get_url = driver.current_url #Сохранение информации о текущем url
url = 'https://www.saucedemo.com/inventory.html' #Сохранение информации о целевом url
assert url == get_url #Сравнение, что текущий url совпадает с целевым
print('URL корректен')
text_products = driver.find_element(By.XPATH, "//span[@class='title']") #Создание объекта Product
value_text_products = text_products.text #Сохранение текста объекта Product
assert value_text_products == 'Products' #Проверка, что на текущей странице есть объект с надписью "Product"
print('Заголовок корректен')