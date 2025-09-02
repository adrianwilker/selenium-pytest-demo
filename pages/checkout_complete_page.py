from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CheckoutCompletePage(BasePage):
  def __init__(self, driver):
    self.driver = driver
    self.page_title = (By.XPATH, "//span[contains(text(), 'Checkout: Complete!')]")
    self.success_message = (By.XPATH, "//h2[@data-test='complete-header']")

  def checkout_successful(self):
    self.exists(self.page_title)
    self.exists(self.success_message)
    assert '/checkout-complete' in self.get_current_url()
  
  def is_checkout_successful(self):
    return self.exists(self.page_title) and self.exists(self.success_message)