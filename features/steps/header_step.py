from time import sleep

from selenium.webdriver.common.by import By
from behave import given, when, then
# from time import sleep
from selenium.webdriver.support import expected_conditions as EC

# from Target_case import driver

# SEARCH_FIELD = (By.ID, 'search')
# SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
HEADER_LINKS = (By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, 'img')


@when('Search for {search_word}')
def search_product(context, search_word):
    # context.driver.find_element(*SEARCH_FIELD).send_keys(search_word)
    # context.driver.find_element(*SEARCH_BTN).click()
    # context.driver.wait_until(EC.presence_of_element_located(*HEADER_LINKS))
    # sleep(10)
    # context.app.header.search_product()
    context.app.header.search_product(search_word)


@when('Click on Cart icon')
def click_cart(context):
    # context.driver.find_element(*CART_ICON).click()
    context.app.header.click_cart()


@then('Verify header has {number} links')
def verify_header_links(context, number):
    print(type(number))
    links = context.driver.find_elements(*HEADER_LINKS)
    print(links)

    # 6 == 6
    assert len(links) == int(number), f'Expected {number} links but got {len(links)}'

@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    # To see ALL listings (comment out if you only check top ones):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(2)
    context.driver.execute_script("window.scrollBy(0,1000)", "")
    # sleep(2)

    # If you ever need to scroll up, use negative numbers: context.driver.execute_script("window.scrollBy(0, -2000)", "")

    products = context.driver.find_elements(*LISTINGS)  # [WebEl1, WebEl2, WebEl3, WebEl4]

    for product in products[:8]:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Product title not shown'
        print(title)
        product.find_element(*PRODUCT_IMG)
