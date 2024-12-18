import time

from playwright.sync_api import Page, expect, Locator


class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
        self.category_link = page.locator("//ul[@class='navbar-nav']/li[3]/a")
        self.add_button = page.locator("//div[@class='card-header border-0']/div[2]/button")
        self.category_name = page.locator("//mat-dialog-container/app-tables/form/div[1]/div/div[1]/div/div/input")
        #self.subcategory_checkbox = page.locator("//mat-dialog-container/app-tables/form/div[1]/div/div[2]/div/div/input")
        #self.subcategory_checkbox = page.locator("//mat-dialog-container/app-tables/form/div[1]/div/div[2]/div/div")
        self.subcategory_checkbox = page.locator("xpath=//input[@id='customCheckMain']")
        self.subcategory_field = page.locator("//mat-dialog-container/app-tables/form/div[1]/div/div[3]/div/ng-select")
        self.subcategory_field_element = page.locator("//mat-dialog-container/app-tables/form/div[1]/div/div[3]/div/ng-select//span[@class='ng-option-label ng-star-inserted']")
        self.accept_button = page.locator("//mat-dialog-container/app-tables/form/div[2]/button[@type='submit']")
        self.cancel_button = page.locator("//mat-dialog-container/app-tables/form/div[2]/button[@type='button']")
        self.pagination = page.locator("//ul[@class='pagination justify-content-end mb-0']")
        self.last_page = page.locator("(//a[@class='page-link'])[last()-1]")
        self.second_to_last_page = page.locator("(//a[@class='page-link'])[last()-2]")
        self.categories_container = page.locator("//div[@class='table-responsive']")
        self.last_category = page.locator("(//div[@class='table-responsive']/table/tbody/tr)[last()]")

    def create_new_category(self, category: str, test_category_present: bool = False):
        #self.page.wait_for_load_state('networkidle')
        self.category_link.click()
        self.add_button.click()
        self.category_name.click()
        self.category_name.fill(category)
        self.accept_button.click()
        self.page.locator("(//a[@class='page-link'])[last()-1]").click()
        self.page.wait_for_load_state('networkidle')
        if test_category_present:
            assert category in self.last_category.inner_text()

    def create_new_sub_category(self, subcategory: str, category: str, test_sub_category_present: bool = False):
        #self.page.wait_for_load_state('networkidle')
        self.category_link.click()
        self.add_button.click()

        # this should be just self.subcategory_checkbox.click() but it's not working as expected
        self.page.evaluate('''(document.evaluate("//input[@id='customCheckMain']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue).click()''')

        self.category_name.click()
        self.category_name.fill(subcategory)

        self.subcategory_field.click()

        self.subcategory_field.locator("//input").type(category)
        self.subcategory_field_element.click()
        self.accept_button.click()
        self.page.wait_for_timeout(3000)
        self.page.locator("(//a[@class='page-link'])[last()-1]").click()
        self.page.wait_for_load_state('networkidle')
        if test_sub_category_present:
            assert subcategory in self.last_category.inner_text()
            assert category in self.last_category.inner_text()
