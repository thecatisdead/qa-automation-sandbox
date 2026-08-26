from playwright.sync_api import Page, expect


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title_heading = page.locator("[data-test='title']")

        self.first_item_add_button = page.locator(
            "[data-test='add-to-cart-sauce-labs-backpack']"
        )

        self.second_item_add_button = page.locator(
            "[data-test='add-to-cart-sauce-labs-bike-light']"
        )

        self.description_add_item_button = page.locator("[data-test='add-to-cart']")

        self.third_item_link = page.locator("[data-test='inventory-item-name']").nth(0)

        self.back_to_products_button = page.locator("[data-test='back-to-products']")

        self.react_burger_menu_button = page.get_by_role("button", name="Open Menu")

        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")

        self.sort_dropdown = page.locator(".product_sort_container")

    def verify_on_inventory_page(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")
        expect(self.title_heading).to_have_text("Products")

    def add_first_item_to_cart(self):
        self.first_item_add_button.click()

    def add_second_item_to_cart(self):
        self.second_item_add_button.click()

    def back_to_inventory(self):
        self.back_to_products_button.click()

    def view_item_description(self):
        self.third_item_link.click()

    def add_item_from_description(self):
        self.description_add_item_button.click()

    def logout(self):
        self.react_burger_menu_button.click()
        self.page.get_by_role("link", name="Logout").click()

    def verify_cart_count(self, expected_count: str):
        expect(self.cart_badge).to_have_text(expected_count)

    def go_to_cart(self):
        self.page.locator(".shopping_cart_link").click()

    def sort_by(self, option: str):
        self.sort_dropdown.select_option(option)

    def get_product_names(self):
        return self.page.locator(
            "[data-test='inventory-item-name']"
        ).all_text_contents()

    def get_product_prices(self):
        prices = self.page.locator(
            "[data-test='inventory-item-price']"
        ).all_text_contents()

        return [float(price.replace("$", "")) for price in prices]
