#Импортирование вебдрайвера
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install())) #Создание объекта driver для работы с Google Chrome
base_url = 'https://www.saucedemo.com/' #Базовый URL
driver.get(base_url) #Открыть ссылку
driver.set_window_size(1920, 1080) #Установить разрешение окна
