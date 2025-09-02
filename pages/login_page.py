from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

  def __init__(self, driver):
    self.driver = driver
    self.username_field = (By.CSS_SELECTOR, "input[data-test=username]")
    self.password_field = (By.CSS_SELECTOR, "input[data-test=password]")
    self.login_button = (By.CSS_SELECTOR, "input[data-test=login-button]")
    self.error_message = (By.XPATH, "//h3[@data-test='error']")

  def login(self, username, password):
    self.write(self.username_field, username)
    self.write(self.password_field, password)
    self.click(self.login_button)

  def is_login_failed(self, expected_error_message=None):
    if expected_error_message is not None:
      return self.exists(self.error_message) and self.get_text(self.error_message) == expected_error_message
    else:
      return self.exists(self.error_message)

  #def check_login_error(self):
  #  self.exists(self.error_message)

  #def check_error_message_text(self, expected_text):
  #  actual_text = self.get_text(self.error_message)
  #  assert actual_text == expected_text, f"O texto retornado foi '{actual_text}', mas era esperado que fosse '{expected_text}'."