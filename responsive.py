import os
import shutil
import time
import math
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class ResponsiveScreenShot:

    def __init__(self, urls, sizes=[480, 960, 1366, 1920], browser_height=1027):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.urls = urls
        self.sizes = sizes
        self.browser_height = browser_height

    def create_folder_by_url(self, url):
        name = url.split("/")[2].replace(" ", "_").replace(".", "_")
        if name == None or name == "":
            name = "Ananymous_website"
        path = f"./res-screenshots/{name}"
        if os.path.exists(path):
            print("Deleted!")
            shutil.rmtree(path)
        os.makedirs(path)
        return name

    def take_screenshot(self, url):
        self.browser.get(url)
        self.browser.maximize_window()
        folder_name = self.create_folder_by_url(url)
        for size in self.sizes:
            self.browser.set_window_size(size, self.browser_height)
            self.browser.execute_script("""
                      window.scrollTo(0, 0);
                    """)
            time.sleep(2)
            scroll_height = self.browser.execute_script("""
                      return document.body.scrollHeight;
                    """)
            total_section = math.ceil(scroll_height / self.browser_height)
            for section in range(total_section + 1):
                section_height = section * self.browser_height
                self.browser.execute_script(f"""
                        window.scrollTo(0, {section_height});
                      """)
                self.browser.save_screenshot(
                    f"res-screenshots/{folder_name}/{size}x{section}.png")
                time.sleep(3)

    def start(self):
        for url in self.urls:
            self.take_screenshot(url)

    def finish(self):
        self.browser.quit()
