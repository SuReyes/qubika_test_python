from playwright.sync_api import Page, expect, Locator


class LogInPage:
    def __init__(self, page: Page):
        self.page = page
        self.login_username_field = page.locator("//form/div[1]/div/input")
        self.login_password_field = page.locator("//form/div[2]/div/input")
        self.login_button = page.locator("//form/div[4]/button")
        self.login_error = page.locator("//div[@class='overlay-container']/div/div")
        self.checkbox = page.locator("//div[@class='custom-control custom-control-alternative custom-checkbox']/input")

    def navigate(self):
        self.page.goto('https://club-administration.qa.qubika.com/#/auth/login')

    def login(self, username: str, password: str, credentials_error: bool=False):
        #self.page.wait_for_load_state('networkidle')
        #self.login_option.hover()
        self.login_username_field.click()
        self.login_username_field.fill(username)
        self.login_password_field.click()
        self.login_password_field.fill(password)
        self.login_button.click()
        #expect(self.login_error).to_be_visible()
        if credentials_error:
            assert self.login_error.inner_text() == 'Usuario o contraseña incorrectos'
