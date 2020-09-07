from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class GoogleKeywordScreenshooter():
    """
    """

    def __init__(self, keyword, screenshot_dir, max_pages, *args):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.keyword = keyword
        self.search_bar_class = "gLFyf"
        self.screenshot_dir = screenshot_dir
        self.max_pages = max_pages
        self.filter_by_class_names = args

    def start(self):
        self.browser.get("https://google.com")
        search_bar = self.browser.find_element_by_class_name(
            self.search_bar_class)
        search_bar.send_keys(self.keyword)
        search_bar.send_keys(Keys.ENTER)

        # Useful when working with js generated sites
        shitty_elements = []
        try:
            shitty_elements = self.filter_elements_by_class_name()
            if(shitty_elements):
                self.browser.execute_script(
                    """
                    shitty_elements = arguments[0]
                    shitty_elements.forEach(s => {
                        s.remove();
                    })""", shitty_elements
                )
        except Exception:
            pass

        # Find elements from the browser with class "g"
        search_results = self.browser.find_elements_by_class_name("g")
        for index, search_result in enumerate(search_results):
            search_result.screenshot(
                f"{self.screenshot_dir}/{ self.keyword }x{ index }.png")

    def filter_elements_by_class_name(self):
        elements_to_filter = []
        for class_name in self.filter_by_class_names:
            el = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, class_name))
            )
            elements_to_filter.append(el)
        return elements_to_filter

    def finish(self):
        self.browser.quit()
