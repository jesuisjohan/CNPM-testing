import random

import VL1.constants as const
import os
import time
from selenium import webdriver


class VL1(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\SeleniumDrivers",
                 teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(VL1, self).__init__(options=options)
        self.implicitly_wait(const.WAIT_TIME)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def scroll_to_bottom(self):
        """
        Browse Menu 1: Browse the entire menu
        :return: void
        """
        self.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def go_to_top(self):
        """
        Browse Menu 2: Go back to the top of website
        :return:
        """
        time.sleep(3)  # wait for people prepare to go to top
        go_to_top_button = self.find_element_by_css_selector(
            'button[title="Go to top"]'
        )
        go_to_top_button.click()

    def open_detail(self):
        """
        Open detail 1:
        :return:
        """
        main_products = self.find_elements_by_class_name("open-mini-zone")
        chosen_one = main_products[random.randint(0,len(main_products))]
        chosen_one.click()

