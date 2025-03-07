# Импортирование библиотек и пользовательских классов
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from authorization import LoginPage
from open_chrome import OpenChrome


# Создание класса для тестирования с наследованием
class Test(OpenChrome):

    #Метод авторизации
    def authorization(self, login_name, password_name):
        login = LoginPage(self.driver)
        login.enter_login(login_name)
        login.enter_password(password_name)
        login.click_login_button()
        print('Вы авторизовались')

    # Выбираем продукт из каталога
    def select_product(self, name_product):
        add_to_cart_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="add-to-cart-{name_product}"]')))
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
print('Тест стартовал')
start_test.open_browser()
start_test.authorization('standard_user', 'secret_sauce')
start_test.select_product('sauce-labs-backpack')
start_test.go_to_cart()
start_test.checking_in_cart()
print('Тест завершился')