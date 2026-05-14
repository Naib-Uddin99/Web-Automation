from pages.login_page import LoginPage


def test_login_success(driver):
    driver.get("https://qa-sms-panel.netlify.app/signin")   # change this URL

    login_page = LoginPage(driver)

    login_page.login("admin", "password123")  # change credentials

    assert login_page.is_login_successful(), "Login failed!"

