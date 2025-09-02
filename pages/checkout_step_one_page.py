import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutStepOnePage(BasePage):
  def __init__(self, driver):
    self.driver = driver
    self.first_name = (By.XPATH, "//input[@data-test='firstName']")
    self.last_name = (By.XPATH, "//input[@data-test='lastName']")
    self.postal_code = (By.XPATH, "//input[@data-test='postalCode']")
    self.continue_button = (By.XPATH, "//*[@value='Continue' and @data-test='continue']")
    self.error_message = (By.XPATH, "//h3[@data-test='error']")

  def send_checkout_information(self, first_name, last_name, postal_code):
    self.write(self.first_name, first_name)
    self.write(self.last_name, last_name)
    self.write(self.postal_code, postal_code)
    self.click(self.continue_button)

  def check_error_message_text(self):
    return self.find_element(self.error_message).text