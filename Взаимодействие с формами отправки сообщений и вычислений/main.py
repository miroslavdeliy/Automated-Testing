from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.lambdatest.com/selenium-playground/simple-form-demo'
driver.get(base_url)
driver.set_window_size(1920,1080)

#Помещаем в поле Single Input Field сообщение и Клик по кнопке Get Checked Value
message = 'Hello, world!'
input_message = driver.find_element(By.XPATH, '//input[@id="user-message"]').send_keys(message)
show_input_button = driver.find_element(By.XPATH, '//*[@id="showInput"]').click()

#Проверка, что текст совпал
check_message = driver.find_element(By.XPATH, "//p[@id='message']").text
assert check_message == message, 'Ошибка! Текст не совпал!'
print('Текст совпал')

#Помещение в переменные числа для сложения
first_value = 1991
second_value = 31
sum_result = first_value + second_value

#Ввод чисел в поля и нажатие на кнопку Get Sum
input_first_value = driver.find_element(By.XPATH, '//*[@id="sum1"]').send_keys(first_value)
input_second_value = driver.find_element(By.XPATH, '//*[@id="sum2"]').send_keys(second_value)
get_sum_button = driver.find_element(By.XPATH, '//*[@id="gettotal"]/button').click()

#Проверка, что сумма совпала
result_message = driver.find_element(By.XPATH, '//*[@id="addmessage"]').text
assert sum_result == int(result_message), 'Ошибка! Сумма не совпадает!'
print('Сумма совпала')