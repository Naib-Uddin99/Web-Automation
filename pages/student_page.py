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
    department_dropdown_filter = (By.XPATH, "//button[@role='combobox']")
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

    next_button = (
        By.XPATH,
        "//button[normalize-space()='Next']"
    )

    def select_random_department_from_filter(self):

        # Click department dropdown
        self.driver.find_element(*self.department_dropdown_filter).click()

        time.sleep(1)

        # Get all department options
        departments = self.driver.find_elements(*self.dropdown_options)
        random_department = random.choice(departments)

        selected_department = random_department.text


        # Click using JavaScript (VERY IMPORTANT)
        self.driver.execute_script(
            "arguments[0].click();",
            random_department
        )

        time.sleep(2)

        return selected_department

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
        time.sleep(5)

    def click_next_page(self):

        # Find Next button
        next_btn = self.driver.find_element(*self.next_button)

        # Check if disabled
        is_disabled = next_btn.get_attribute("disabled")

        # If disabled
        if is_disabled:
            print("Next button is disabled")
            return "disabled"

        # Click button
        next_btn.click()

        print("Clicked Next button")

        time.sleep(1)

        return "clicked"

    def get_table_data_as_dictionary(self):
        """
        Returns all table row data as list of dictionaries
        """

        table_data = []

        # Get all rows
        rows = self.driver.find_elements(
            By.XPATH,
            "//tbody/tr"
        )

        # Loop through each row
        for row in rows:
            # Get all td values except action buttons
            columns = row.find_elements(By.XPATH, "./td")

            row_data = {
                "name": columns[0].text,
                "email": columns[1].text,
                "department": columns[2].text,
                "student_id": columns[3].text,
                "age": columns[4].text
            }

            table_data.append(row_data)

        return table_data

    def click_filter_button(self):

        self.driver.find_element(
            By.XPATH,
            "//button[text()='Filter']"
        ).click()

        time.sleep(2)