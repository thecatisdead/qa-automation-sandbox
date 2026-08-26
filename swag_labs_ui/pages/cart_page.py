from playwright.sync_api import Page, expect


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.continue_shopping_button = page.locator("[data-test='continue-shopping']")
        self.checkout_button = page.locator("[data-test='checkout']")

        self.first_item_remove_button = page.locator(
            "[data-test='remove-sauce-labs-backpack']"
        )

    def click_continue_shopping(self):
        self.continue_shopping_button.click()

    def remove_first_item_to_cart(self):
        self.first_item_remove_button.click()
