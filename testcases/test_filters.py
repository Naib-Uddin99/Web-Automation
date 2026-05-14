from pages import student_page
from pages.login_page import LoginPage
from pages.student_page import StudentPage



def test_department_filter(driver):
    driver.get("https://qa-sms-panel.netlify.app/signin")   # change this URL

    login_page = LoginPage(driver)
    student_page = StudentPage(driver)

    login_page.login("admin", "password123")  # change credentials


    student_page.select_page_size(100)



