import conftest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys

class BasePage:
  def __init__(self):
    self.driver = conftest.driver

  def find_element(self, locator):
    return self.driver.find_element(*locator)
  
  def find_elements(self, locator):
    return self.driver.find_elements(*locator)
  
  def write(self, locator, text):
    element = self.wait_element_appear(locator)
    element.send_keys(text)

  def click(self, locator):
    element = self.wait_element_appear(locator)
    element.click()
  
  def exists(self, locator):
    try:
      return self.find_element(locator).is_displayed()
    except Exception:
      return False
  
  def not_exists(self, locator):
    return len(self.find_elements(locator)) == 0

  def get_text(self, locator):
    self.wait_element_appear(locator)
    return self.find_element(locator).text
  
  def wait_element_appear(self, locator, timeout=10):
    return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
  
  def double_click(self, locator):
    element = self.wait_element_appear(locator)
    ActionChains(self.driver).double_click(element).perform()

  def right_click(self, locator):
    element = self.wait_element_appear(locator)
    ActionChains(self.driver).context_click(element).perform()

  def press_key(self, locator, key):
    element = self.find_element(locator)
    if key=="ENTER":
      element.send_keys(Keys.ENTER)
    elif key == "SPACE":
      element.send_keys(Keys.SPACE)

  def get_current_url(self):
    return self.driver.current_url

  def access_page(self, page_url):
    self.driver.get(page_url)