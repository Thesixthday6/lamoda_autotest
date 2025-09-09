import undetected_chromedriver as uc 
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = uc.Chrome()


def search_product(name='Худи'):
    names_list = []
    driver.get(r'https://www.lamoda.ru')
    time.sleep(5)
    input_form = driver.find_element(By.TAG_NAME, "input")
    input_form.click()
    input_form.send_keys(name)
    time.sleep(1)
    input_form.send_keys(Keys.ENTER)
    time.sleep(5)
    names = driver.find_elements(By.CSS_SELECTOR, ".x-product-card-description__product-name")
    for name in names:
        names_list.append(name.text)
    driver.quit()
    return names_list


if __name__ == '__main__':
    names_list = search_product()
    print(names_list)
    
