
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time
import re


INITIAL_PAGE = 1
URL = 'https://www.farfetch.com/ru/shopping/women/clothing-1/items.aspx?page='
LINK = "_5ce6f6"
COUNTER = 0

list_price = []
list_categories = []
list_ids = []
list_discounts = []


def parse(driver, page):
    global COUNTER
    driver.get(URL + str(page))
    time.sleep(4)
    cards = driver.find_elements_by_xpath('//*[@data-test = "productCard"]')
    for el in cards:
        list_ids.append(get_item_id(el))
        list_categories.append(get_item_category(el))
        list_price.append(get_item_price(el))
        list_discounts.append(get_item_discount(el))
        COUNTER += 1
        if COUNTER >= 200:
            return print(COUNTER, list_ids, list_discounts, list_categories, list_price, sep='\n')
    page += 1
    parse(driver, page)


def get_item_id(item):
    item = str(item.find_elements_by_class_name(LINK).pop().get_attribute('href'))
    _id = re.search(r'item-?\d+', item).group(0)
    return _id


def get_item_price(item):
    price = item.find_element_by_xpath('.//span[@data-test = "price"]')
    price = price.text
    return price


def get_item_category(item):
    cat = item.find_element_by_xpath('.//p[@data-test = "productDescription"]')
    cat = cat.text
    return cat


def get_item_discount(item):
    try:
        item = item.find_element_by_xpath('.//span[@data-test = "initialPrice"]')
        discount = item.text
    except NoSuchElementException:
        discount = 'No discount'
    return discount


def make_dataframe():
    df = pd.DataFrame()
    df["id"] = list_ids
    df["price"] = list_price
    df["discount"] = list_discounts
    df["category"] = list_categories
    df.to_csv('myfile.csv', index=False)


def main():
    with webdriver.Chrome(executable_path=ChromeDriverManager().install()) as driver:
        parse(driver, INITIAL_PAGE)
        make_dataframe()


if __name__ == '__main__':
    main()