from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

#Открыть браузер и перейти по ссылке
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.set_window_size(1920,1080)

#Создать экземпляр класса Faker и ввести в поле логина случайный username
fake = Faker("en_US")
user_name = driver.find_element(By.XPATH, '//*[@id="user-name"]')
user_name.send_keys(fake.user_name())
print('Введен логин')