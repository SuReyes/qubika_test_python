from uuid import uuid4

from playwright.sync_api import sync_playwright

from apis.user_api import create_user
from pages.dashboardpage import DashboardPage
from pages.loginpage import LogInPage

#
# def test_login_error():
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False, slow_mo=50)
#         page = browser.new_page()
#         home = LogInPage(page)
#
#         home.navigate()
#         home.login('user', 'pass', credentials_error=True)

#
# def test_login_success():
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False, slow_mo=50)
#         page = browser.new_page()
#         home = LogInPage(page)
#
#         home.navigate()
#         home.login('test.qubika@qubika.com', '12345678', credentials_error=False)


def test_exercise_two():
    with sync_playwright() as playwright:
        username = f"test.qubika+{uuid4()}@qubika.com"
        password = "12345678"
        browser = playwright.chromium.launch(headless=False, slow_mo=50)
        page = browser.new_page()
        status_code, response = create_user(username, password)
        assert status_code == 201, "Error creating user"

        home = LogInPage(page)
        home.navigate()
        home.login(username, password, credentials_error=False)

        dashboard = DashboardPage(page)
        category = str(uuid4())
        dashboard.create_new_category(category, True)

        subcategory = str(uuid4())
        dashboard.create_new_sub_category(subcategory, category, True)





