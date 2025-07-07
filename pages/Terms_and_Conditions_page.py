from pages.base_page import Page


class TermsConditions(Page):

    def verify_TC_opened(self):
        self.wait_for_url_contains('terms-conditions')