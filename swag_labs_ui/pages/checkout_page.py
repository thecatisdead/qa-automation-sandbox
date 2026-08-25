from playwright.sync_api import Page, expect


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_input = page.locator("[data-test='firstName']")
        self.last_name_input = page.locator("[data-test='lastName']")
        self.postal_code_input = page.locator("[data-test='postalCode']")
        self.continue_button = page.get_by_role("button", name="Continue")
        self.finish_button = page.get_by_role("button", name="Finish")
        self.success_message = page.locator("[data-test='complete-header']")
        self.error_message = page.locator('[data-test="error"]')

    def fill_shipping_info(self, first_name: str, last_name: str, postal_code: str):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)
        self.continue_button.click()

    def fail_checkout(self):
        self.continue_button.click()

    def complete_checkout(self):
        self.finish_button.click()

    def verify_order_success(self):
        expect(self.success_message).to_have_text("Thank you for your order!")

    # failed path
    def verify_error_message(self, expected_text: str):
        expect(self.error_message).to_be_visible()
        expect(self.error_message).to_contain_text(expected_text)
