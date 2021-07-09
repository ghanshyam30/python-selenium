from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#driver = webdriver.Firefox(executable_path="/home/thebadcoder/MyWorkSpace/Testing/python_selenium/code/drivers/geckodriver-v0.29.1-linux32/geckodriver")
driver = webdriver.Firefox()
url = "https://www.amazon.in"
driver.get(url)


## Validation
page_title = driver.title
print("Page title: ",page_title)

## input something
search_for_product = "OnePlus Nord CE 5G"

search_box = driver.find_element_by_xpath('//input[@id="twotabsearchtextbox"]')
search_box.send_keys(search_for_product)

## click something
search_button = driver.find_element_by_id("nav-search-submit-button")
search_button.click()

## Wait for Search results
wait_for_serch_element = "a-section a-spacing-small a-spacing-top-small"
try:
    element_to_expect = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//div[@class='a-section a-spacing-small a-spacing-top-small']")))

except:
    print("There was an exception")

## Name to check in list and click on
## OnePlus Nord CE 5G (Charcoal Ink, 8GB RAM, 128GB Storage)
product_name = "OnePlus Nord CE 5G (Charcoal Ink, 8GB RAM, 128GB Storage)"


print("Automation completed")
driver.close()
