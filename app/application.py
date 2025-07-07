from pages.base_page import Page
from pages.Terms_and_Conditions_page import TermsConditions
from pages.header import Header
from pages.help_page import HelpPage
from pages.main_page import MainPage
from pages.privacy_policy_page import PrivacyPolicyPage
from pages.target_app_page import TargetAppPage
from pages.target_TC_app_page import TargetTCapppage
from pages.search_result_page import SearchResultsPage
from pages.cart_page import CartPage


class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.terms_and_conditions_page = TermsConditions(driver)
        self.cart_page = CartPage(driver)
        self.header = Header(driver)
        self.help_page = HelpPage(driver)
        self.main_page = MainPage(driver)
        self.privacy_policy_page = PrivacyPolicyPage(driver)
        self.target_app_page = TargetAppPage(driver)
        self.target_TC_app_page = TargetTCapppage(driver)
        self.search_results_page = SearchResultsPage(driver)

