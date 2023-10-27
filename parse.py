import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()

s = Service("/home/filemgun/Рабочий стол/silenium/chromedriver")
driver = webdriver.Chrome(service=s)

login = os.getenv('LOGIN')
password = os.getenv('PASS')


def auth() -> None:
    """Log in to your account"""

    button_auth = driver.find_element(By.CSS_SELECTOR, '.button--toW5-square.space--ml-2.button.button--shape-circle.button--type-primary.button--mode-white')
    button_auth.click()
    time.sleep(1)

    input_login = driver.find_element(By.ID, "loginModalForm-identity")
    input_login.clear()
    input_login.send_keys(login)

    input_pass = driver.find_element(By.ID, "loginModalForm-password")
    input_pass.clear()
    input_pass.send_keys(password)

    button_singin = driver.find_element(By.NAME, "form_submit")
    button_singin.click()
    time.sleep(1)


def parse(num: int) -> None:
    """parse of information"""

    items = driver.find_elements(By.CLASS_NAME, "thread-title")
    action = ActionChains(driver)

    action.key_down(Keys.CONTROL).click(items[num]).key_up(Keys.CONTROL).perform()

    driver.switch_to.window(driver.window_handles[1])
    time.sleep(1)
    name_item = driver.find_element(By.XPATH, "//*[@class='text--b size--all-xl size--fromW3-xxl']")
    print(f'Название товара: {name_item.text}')

    try:
        price = driver.find_element(By.XPATH, "//*[@class='threadItemCard-price text--b thread-price']")
        print(f'Цена товара: {price.text}')
    except:
        print('Цена товара не указана')
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print('||//' * 5)


def main():
    driver.get('https://www.pepper.ru/')
    auth()
    for i in range(10):
        parse(i)


if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print(f'Возникла ошибка: {ex}')
    finally:
        driver.close()
        driver.quit()
