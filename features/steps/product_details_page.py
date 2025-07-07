from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

COLOR_OPTIONS = (By.CSS_SELECTOR, "li[class*='CarouselItem'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")


@given('Open target product A-54551690 pages')
def open_target(context):
    context.driver.get(f'https://www.target.com/p/denizen-from-levi-s-men-s-285-relaxed-fit-jeans/-/A-54551690')
    # sleep(8)
    context.driver.wait.until(EC.visibility_of_element_located(SELECTED_COLOR))

@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['Blue Tint', 'Denim Blue', 'Marine', 'Raven']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)  # [webelement1, webelement2, webelement3, webelement4]
    print(colors)

    for c in colors:
        c.click()
        sleep(4)
        selected_color = context.driver.find_element(*SELECTED_COLOR).text  # 'Color\nBlack'
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f"Expected {expected_colors} did not match actual {actual_colors}"