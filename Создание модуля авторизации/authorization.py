# Импортирвание библиотек и пользовательских классов
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Создание класса авторизации с наследованием
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # Метод ввода логина
    def enter_login(self, login):
        username_input = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="user-name"]')))
        username_input.send_keys(login)
        print('Введен логин')

    # Метод ввода пароля
    def enter_password(self, password):
        password_input = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]')))
        password_input.send_keys(password)
        print('Введен пароль')

    # Метод клика на кнопку входа
    def click_login_button(self):
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')
        login_button.click()