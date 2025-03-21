# Импортирование библиотек и классов
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Создание класса для тестирования
class Test():
    # Конструктор класса
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    # Метод открытия браузера
    def open_browser(self):
        base_url = 'https://www.saucedemo.com/'
        self.driver.get(base_url)
        self.driver.set_window_size(1920,1080)
        print('Браузер открылся')


# Создание экземпляра класса и выполнение методов
start_test = Test()
start_test.open_browser()
