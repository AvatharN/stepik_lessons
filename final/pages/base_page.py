from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .locators import BasePageLocators


class BasePage:

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_string_in_current_url(self, string):
        return string in self.browser.current_url

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def check_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), 'Login link not presented'

    def go_to_basket(self):
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_VIEW_BUTTON)
        basket_link.click()

    def go_to_account_page(self):
        account_link = self.browser.find_element(*BasePageLocators.ACCOUNT_LINK)
        account_link.click()

    def logout_user(self):
        logout_link = self.browser.find_element(*BasePageLocators.LOGOUT_LINK)
        logout_link.click()

    def is_user_logged_in(self):
        return self.is_element_present(*BasePageLocators.ACCOUNT_LINK)

    def is_user_logged_out(self):
        return self.is_element_present(*BasePageLocators.LOGIN_LINK)

    def check_is_user_logged_in(self):
        assert self.is_user_logged_in() is True, 'User is not logged in'

    def check_is_user_logged_out(self):
        assert self.is_user_logged_out() is True, 'User is logged in'
