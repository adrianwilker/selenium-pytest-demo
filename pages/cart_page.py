from pages.base_page import BasePage
import conftest
from selenium.webdriver.common.by import By


class CartPage(BasePage):
  def __init__(self, driver):
    self.driver = driver
    self.item_for_sale = (By.XPATH, "//*[@data-test='inventory-item-name' and text()='{}']")
    self.continue_shopping_button = (By.XPATH, "//button[@data-test='continue-shopping']")
    self.checkout_button = (By.XPATH, "//button[contains(text(), 'Checkout') and @data-test='checkout']")
    self.remove_button = (By.XPATH, "//div[@class='inventory_item_name'{filter}]/ancestor::div[@class='cart_item_label']//button[contains(., 'Remove')]")

  def product_exists(self, product):
    return self.exists((self.item_for_sale[0], self.item_for_sale[1].format(product)))
  
  def check_product_nonexistence(self, product):
    self.not_exists((self.item_for_sale[0], self.item_for_sale[1].format(product)))

  def click_continue_shopping(self):
    self.click(self.continue_shopping_button)

  def checkout(self):
    self.click(self.checkout_button)

  def remove_all_products(self):
    xpath = self.remove_button[1].format(filter="")
    elements = self.find_elements((self.remove_button[0], xpath))
    for el in elements:
      el.click()
  
  def remove_product(self, product):
    xpath = self.remove_button[1].format(filter=f" and text()='{product}'")
    self.click((self.remove_button[0], xpath))
