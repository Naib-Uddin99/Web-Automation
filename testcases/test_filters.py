from pages import student_page
from pages.login_page import LoginPage
from pages.student_page import StudentPage



def test_department_filter(driver):

    driver.get("https://qa-sms-panel.netlify.app/signin")

    login_page = LoginPage(driver)
    student_page = StudentPage(driver)

    # Login
    login_page.login("admin", "password123")

    # Select Page Size
    student_page.select_page_size("100")



    # Select Random Department
    selected_department = student_page.select_random_department_from_filter()

    print(f"Selected Department: {selected_department}")

    # Click Filter Button
    student_page.click_filter_button()

    # Validate All Pages
    while True:

        # Get Table Data
        table_data = student_page.get_table_data_as_dictionary()

        # Assertion
        for row in table_data:

            actual_department = row["department"]

            print(
                f"Expected: {selected_department} | "
                f"Actual: {actual_department}"
            )

            assert actual_department == selected_department, (
                f"Department mismatch. "
                f"Expected: {selected_department}, "
                f"Found: {actual_department}"
            )

        # Go To Next Page
        has_next = student_page.click_next_page()

        # # Stop if Next button disabled
        if has_next == "disabled":
            print("Reached last page")
            break







