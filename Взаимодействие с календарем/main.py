import time
from datetime import datetime
from datetime import timedelta
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
driver.set_window_size(1920, 1080)

#Выбор поля ввода даты и его очистка
date_input = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
date_input.send_keys(Keys.CONTROL + 'a')
date_input.send_keys(Keys.DELETE)

time.sleep(1)

#Установление даты, на 10 дней больше текущей
current_day = datetime.now() + timedelta (days=10)
date_input.send_keys(current_day.strftime("%m.%d.%Y"))