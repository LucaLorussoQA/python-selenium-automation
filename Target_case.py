from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# open the url
driver.get('https://www.target.com')

#Click Account button
driver.find_element(By.XPATH, "//span[@class='sc-43f80224-3 fBDEOp h-margin-r-x3']").click()
sleep(3)
# Click SignIn btn from side navigation
driver.find_element(By.XPATH, "//button[@class='styles_ndsBaseButton__W8Gl7 styles_md__X_r95 styles_mdGap__9J0yq styles_fullWidth__3XX6f styles_ndsButton__XOOOH styles_md__Yc3tr styles_filleddefault__7QnWt h-margin-t-x2 h-margin-b-default']").click()
sleep(3)

# Verify SignIn pages opened:
driver.find_element(By.XPATH, "//div[@class='sc-b40687e3-1 jWoDIm']")

# “Sign in or create account” text is shown,
driver.find_element(By.XPATH, "//h1[@class='styles_ndsHeading__HcGpD styles_fontSize1__i0fbt styles_x2Margin__M5gHh h-text-lg h-text-center h-margin-b-tiny']")

# SignIn button is shown (you can just use driver.find_element() to check for element’s presence, no need to assert here)
driver.find_element(By.XPATH, "//button[@class='styles_ndsBaseButton__W8Gl7 styles_lg___H2IL styles_lgGap__bPB7P styles_fullWidth__3XX6f styles_ndsButton__XOOOH styles_lg__T5sAi styles_filleddefault__7QnWt']")

