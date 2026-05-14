import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select


class StudentPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locator of department filter
    department_dropdown_filter = (By.XPATH, "//button[@role='combobox']//span[text()='Filter by department...']")
    # Locator for all dropdown options
    dropdown_options = (
        By.XPATH,
        "//div[@role='option']"
    )
    # Locator
    page_size_dropdown = (
        By.XPATH,
        "//select"
    )

    def select_random_department_from_filter(self):
        self.driver.find_element(*self.department_dropdown_filter).click()
        # Get all dropdown options
        options = self.driver.find_elements(*self.dropdown_options)

        # Choose random option
        random_option = random.choice(options)

        # Get visible text
        option_text = random_option.text

        # Click selected option
        random_option.click()

        print(f"Randomly Selected Department: {option_text}")

        return option_text

    def select_page_size(self, page_size):

        # Wait until dropdown appears
        dropdown = self.wait.until(
            lambda d: d.find_element(*self.page_size_dropdown)
        )

        # Click dropdown
        dropdown.click()

        # Select value
        select = Select(dropdown)
        select.select_by_visible_text(str(page_size))

        print(f"Selected Page Size: {page_size}")
        time.sleep(2)