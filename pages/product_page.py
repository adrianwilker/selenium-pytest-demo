import conftest
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
  def __init__(self, driver):
    self.driver = driver
    self.button_add_to_shopping_cart = (By.XPATH, "//*[contains(text(), 'Add to cart')]")
    self.button_back_to_products = (By.XPATH, "//button[@data-test='back-to-products']")
    self.product_name = (By.XPATH, "//div[@data-test='inventory-item-name']")
    self.product_description = (By.XPATH, "//div[@data-test='inventory-item-desc']")
    self.product_price = (By.XPATH, "//div[@data-test='inventory-item-price']")
    self.product_image = (By.CLASS_NAME, "inventory_details_img")
    self.product_button = (By.ID, "add-to-cart")
    self.shopping_cart_icon = self.shopping_cart_icon = (By.CLASS_NAME, "shopping_cart_link")

  def add_to_shopping_cart(self):
    self.click(self.button_add_to_shopping_cart)

  def back_to_home(self):
    self.click(self.button_back_to_products)

  def get_product_info(self):
    product_name = self.find_element(self.product_name)
    product_description = self.find_element(self.product_description)
    product_price = self.find_element(self.product_price)
    product_image = self.find_element(self.product_image)
    product_button = self.product_button
    return {
            "name": product_name.text,
            "description": product_description.text,
            "price": product_price.text,
            "image": product_image.get_property("src"),
            "button": product_button
        }
  
  def access_shopping_cart(self):
    self.click(self.shopping_cart_icon)