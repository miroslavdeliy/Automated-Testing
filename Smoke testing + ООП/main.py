# Импортирование библиотек и классов
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

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

    # Метод ввода логина
    def enter_login(self, login):
        username_input = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="user-name"]')))
        username_input.send_keys(login)
        print('Введен логин')

    # Метод ввода пароля
    def enter_password(self, password):
        password_input = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]')))
        password_input.send_keys(password)
        print('Введен пароль')

    # Метод нажатия на кнопку логина
    def click_login_button(self):
        login_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]')))
        login_button.click()
        print('Нажата кнопка авторизации')

    # Выбираем продукт из каталога
    def select_product(self):
        add_to_cart_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')))
        add_to_cart_button.click()
        print('Выбран продукт')

    # Переходим в корзину
    def go_to_cart(self):
        shopping_cart_link = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="shopping_cart_container"]/a')))
        shopping_cart_link.click()
        print('Перешли в корзину')

    # Проверка, что находимся в корзине
    def checking_in_cart(self):
        title_text = self.driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span').text
        assert title_text == 'Your Cart', 'Ошибка! Вы не находитесь в корзине!'
        print('Вы в корзине')


# Создание экземпляра класса и выполнение методов
start_test = Test()
start_test.open_browser()
start_test.enter_login('standard_user')
start_test.enter_password('secret_sauce')
start_test.click_login_button()
start_test.select_product()
start_test.go_to_cart()
start_test.checking_in_cart()
