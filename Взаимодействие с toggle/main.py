import time
from os import times

from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://html5css.ru/howto/howto_js_rangeslider.php'
driver.get(base_url)
driver.set_window_size(1920, 1080)

time.sleep(2)

actions = ActionChains(driver)
slider = driver.find_element(By.XPATH, '//*[@id="id1"]')

#Движение ползунка
actions.click_and_hold(slider).move_by_offset(100, 0).release().perform()
print('Ползунок сдвинулся')

#Проверка, что ползунок сдвинулся правильно
value_check = driver.find_element(By.XPATH, '//*[@id="f"]').text
assert value_check == '60', 'Ползунок сдвинулся неправильно!'
print('Ползунок сдвинулся правильно!')