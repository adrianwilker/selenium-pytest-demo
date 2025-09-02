from operator import itemgetter
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from enum import Enum

class SortType(Enum):
    AZ = "az"
    ZA = "za"
    LOHI = "lohi"
    HILO = "hilo"

class HomePage(BasePage):
  def __init__(self, driver):
    self.driver = driver
    self.page_title = (By.XPATH, "//span[@class='title']")
    self.item_for_sale = (By.XPATH, "//*[@data-test='inventory-item-name' and text()='{}']")
    self.button_add_to_cart = (By.XPATH, "//*[@data-test='inventory-item-name' and text()='{}']/ancestor::div[@class='inventory_item']//button[contains(text(), 'Add to cart')]")
    self.shopping_cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    self.item_containers = (By.XPATH, "//div[@data-test='inventory-item']")
    self.item_name = (By.XPATH, ".//div[@data-test='inventory-item-name']")
    self.item_description = (By.XPATH, ".//div[@data-test='inventory-item-desc']")
    self.item_price = (By.XPATH, ".//div[@data-test='inventory-item-price']")
    self.item_button = (By.XPATH, ".//button[contains(@data-test, 'add-to-cart')]")
    self.open_menu_button = (By.ID, "react-burger-menu-btn")
    self.close_menu_button = (By.ID, "react-burger-cross-btn")
    self.logout_link = (By.ID, "logout_sidebar_link")
    self.select_element = (By.XPATH, "//select[@data-test='product-sort-container']")

  def is_logged_in(self):
    return self.exists(self.page_title)
  
  def add_to_shopping_cart(self, product_name):
    self.click((self.button_add_to_cart[0], self.button_add_to_cart[1].format(product_name)))

  def access_product_page(self, product_name):
    item = (self.item_for_sale[0], self.item_for_sale[1].format(product_name))
    self.click(item)

  def access_shopping_cart(self):
    self.click(self.shopping_cart_icon)
  
  def get_products(self):
    products = []
    items = self.find_elements(self.item_containers)
    
    for item in items:
      item_name = item.find_element(*self.item_name).text
      item_description = item.find_element(*self.item_description).text
      item_price = item.find_element(*self.item_price).text
      item_button = item.find_element(*self.item_button)
      products.append({
            "item_name": item_name,
            "item_description": item_description,
            "item_price": float(item_price.replace("$","")),
            "item_button": item_button
        })
    return products
  
  def open_menu(self):
    self.click(self.open_menu_button)

  def close_menu(self):
    self.click(self.close_menu_button)

  def logout(self):
    self.click(self.logout_link)

  def reorder_products(self, sort_type: SortType):
    element = self.find_element(self.select_element)
    select = Select(element)
    select.select_by_value(sort_type.value)

  @staticmethod
  def sorted_products(products, sort_type: SortType):
    clean = [{k: v for k, v in p.items() if k != "item_button"} for p in products]

    if sort_type == SortType.AZ:
      return sorted(clean, key=itemgetter("item_name"))
    elif sort_type == SortType.ZA:
      return sorted(clean, key=itemgetter("item_name"), reverse=True)
    elif sort_type == SortType.LOHI:
      return sorted(clean, key=itemgetter("item_price"))
    elif sort_type == SortType.HILO:
      return sorted(clean, key=itemgetter("item_price"), reverse=True)
    else:
      raise ValueError("Invalid sort type")
  
  def remove_button_key_from_products(self, products):
    return [
      {k: v for k, v in prod.items() if k != "item_button"}
      for prod in products
    ]