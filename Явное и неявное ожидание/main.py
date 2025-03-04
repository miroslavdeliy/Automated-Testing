import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

#Открыть браузер
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.set_window_size(1920,1080)

#Авторизация
user_name = driver.find_element(By.ID, 'user-name')
user_name.send_keys("standard_user")
password = driver.find_element(By.ID, 'password')
password.send_keys("secret_sauce")
button_login = driver.find_element(By.ID, 'login-button')
button_login.click()

#Пользовательское меню
print('Приветствую тебя в нашем интернет - магазине')
print('Выбери один из следующих товаров и укажи его номер:\
      \n1 - Sauce Labs Backpack,\n2 - Sauce Labs Bike Light,\
      \n3 - Sauce Labs Bolt T-Shirt,\n4 - Sauce Labs Fleece Jacket,\
      \n5 - Sauce Labs Onesie,\n6 - Test.allTheThings()T-Shirt(Red):\n')
users_choice = input()
if users_choice == '1':
    product_name = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div').text
    print(product_name)
    product_price = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div').text
    print(product_price)
    select_product = driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']").click()
    print('Выбран продукт')
elif users_choice == '2':
    product_name = driver.find_element(By.XPATH, '//*[@id="item_0_title_link"]/div').text
    print(product_name)
    product_price = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[2]/div[2]/div[2]/div').text
    print(product_price)
    select_product = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
    print('Выбран продукт')
elif users_choice == '3':
    product_name = driver.find_element(By.XPATH, '//*[@id="item_1_title_link"]/div').text
    print(product_name)
    product_price = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[3]/div[2]/div[2]/div').text
    print(product_price)
    select_product = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    print('Выбран продукт')
elif users_choice == '4':
    product_name = driver.find_element(By.XPATH, '//*[@id="item_5_title_link"]/div').text
    print(product_name)
    product_price = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[4]/div[2]/div[2]/div').text
    print(product_price)
    select_product = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]').click()
    print('Выбран продукт')
elif users_choice == '5':
    product_name = driver.find_element(By.XPATH, '//*[@id="item_2_title_link"]/div').text
    print(product_name)
    product_price = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[5]/div[2]/div[2]/div').text
    print(product_price)
    select_product = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-onesie"]').click()
    print('Выбран продукт')
elif users_choice == '6':
    product_name = driver.find_element(By.XPATH, '//*[@id="item_3_title_link"]/div').text
    print(product_name)
    product_price = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[6]/div[2]/div[2]/div').text
    print(product_price)
    select_product = driver.find_element(By.XPATH, '//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]').click()
    print('Выбран продукт')
else:
    print('Неправильно выбран пункт меню! Выберите из представленных выше!')

# Переход в корзину
cart = driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']")
cart.click()
print("Перешли в корзину")

# Проверка название товара в корзине
cart_product_name = driver.find_element(By.XPATH, '//div[@class="inventory_item_name"]').text
print(cart_product_name)
assert product_name == cart_product_name, 'Ошибка! Название товара в корзине некорректно!'
print("Название товара в корзине корректно")

# Проверка цены товара в корзине
cart_product_price = driver.find_element(By.XPATH, '//div[@class="inventory_item_price"]').text
print(cart_product_price)
assert product_price == cart_product_price, 'Ошибка! Цена товара в корзине некорректна!'
print('Цена товара в корзине корректна')

# Нажатие на кнопку checkout
checkout = driver.find_element(By.XPATH, "//*[@id='checkout']").click()
print('Нажата кнопка checkout')

fake = Faker("en_US")

# Ввод фейковых данных
first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
first_name.send_keys(fake.first_name())
print('Введено First Name')
last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
last_name.send_keys(fake.last_name())
print('Введено Last Name')
postal_code = driver.find_element(By.XPATH, "//input[@id='postal-code']")
postal_code.send_keys(fake.postcode())
print('Введено Postal Code')

time.sleep(3)

# Нажать на кнопку continue
button_continue = driver.find_element(By.XPATH, "//input[@id='continue']")
button_continue.click()
print('Нажата continue')

# Проверка названия товара на итоговой странице
finish_product_name = driver.find_element(By.XPATH, '//div[@class="inventory_item_name"]').text
print(finish_product_name)
assert product_name == finish_product_name, 'Ошибка! Название товара на итоговой странице некорректно!'
print("Название товара на итоговой странице корректно")

# Проверка цены товара на итоговой странице
finish_product_price = driver.find_element(By.XPATH, '//div[@class="inventory_item_price"]').text
print(finish_product_price)
assert product_price == finish_product_price, 'Ошибка! Цена товара на итоговой странице некорректна!'
print('Цена товара на итоговой странице корректна')

# Проверка итоговой цены
summary_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[6]").text
print(summary_price)
item_total = "Item total: " + finish_product_price
print(item_total)
assert summary_price == item_total, 'Ошибка! Итоговая сумма не совпала!'
print('Итоговая сумма совпала')

# Нажать на кнопку Finish
button_finish = driver.find_element(By.XPATH, "//*[@id='finish']")
button_finish.click()
print("Нажата кнопка Finish")

#Проверка, что заказ оформлен
checkout_complete = driver.find_element(By.XPATH, "//*[contains(text(), 'Thank you for your order!')]")
value_checkout_complete = checkout_complete.text
print(value_checkout_complete)
assert value_checkout_complete == 'Thank you for your order!', 'Ошибка! Информация об оформлении заказа некорректна!'
print('Информация об оформлении заказа корректна')