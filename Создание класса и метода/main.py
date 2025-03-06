# Импортирование библиотек и классов
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Создание класса для тестирования
class Test():
    # Конструктор класса
    def __init__(self):
        self.driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    # Метод открытия браузера
    def test_select_product(self):
        base_url = 'https://www.saucedemo.com/'
        self.driver.get(base_url)
        self.driver.set_window_size(1920,1080)
        print('Браузер открылся')


# Создание экземпляра класса и выполнение методов
start_test = Test()
start_test.test_select_product()
