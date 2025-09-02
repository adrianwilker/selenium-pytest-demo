from pages.base_page import BasePage
import conftest
from selenium.webdriver.common.by import By

class CheckoutStepTwoPage(BasePage):
  def __init__(self, driver):
    self.driver = driver
    self.finish_button = (By.XPATH, "//button[@data-test='finish']")
    self.subtotal = (By.XPATH, "//div[@data-test='subtotal-label']")
    self.tax = (By.XPATH, "//div[@data-test='tax-label']")
    self.total = (By.XPATH, "//div[@data-test='total-label']")

  def finish(self):
    self.click(self.finish_button)

  def get_subtotal(self):
    subtotal = self.get_text(self.subtotal)
    subtotal = float(subtotal.split("$")[1])
    return subtotal
  
  def get_tax(self):
    tax = self.get_text(self.tax)
    tax = float(tax.split("$")[1])
    return tax
  
  def get_total(self):
    total = self.get_text(self.total)
    total = float(total.split("$")[1])
    return total