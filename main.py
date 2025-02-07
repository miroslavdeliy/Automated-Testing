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
password = driver.find_element(By.XPATH, "//*[@id='password']") #Создание объекта поля ввода пароля
password.send_keys("secret_sauce") #ввести данные в поле пароля
