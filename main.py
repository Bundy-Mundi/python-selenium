from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

KEYWORD = "hello"

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://google.com")
search_bar_class = "gLFyf"
search_bar = browser.find_element_by_class_name(search_bar_class)

# Type keyword and enter
search_bar.send_keys(KEYWORD)
search_bar.send_keys(Keys.ENTER)

# Useful when working with js generated sites
elements = WebDriverWait(browser, 10).until(EC.presence_of_element_located(By.CLASS_NAME, "g-blk"))

# Find elements from the browser with class "g"
search_results = browser.find_elements_by_class_name("g")

for index, search_result  in enumerate(search_results):
    search_result.screenshot(f"screenshots/{ KEYWORD }x{ index }.png")

    # Excluding search_result with specific class name
    # class_name = search_result.get_attribute("class")
    # if <class name> not in class_name:
        # search_result.screenshot(f"screenshots/{ KEYWORD }x{ index }.png")

# browser.quit()