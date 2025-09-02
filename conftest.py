import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import logging
from datetime import datetime
import os
import stat
from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage

driver: webdriver.Remote

@pytest.fixture(scope="session")
def base_url():
    return "https://www.saucedemo.com/"

@pytest.fixture()
def driver(base_url):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-gpu")
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }
    options.add_experimental_option("prefs", prefs)
    driver_dir = ChromeDriverManager().install()
    driver_path = os.path.join(driver_dir, "chromedriver-linux64", "chromedriver")
    st = os.stat(driver_path)
    os.chmod(driver_path, st.st_mode | stat.S_IEXEC)
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get(base_url)
    yield driver
    driver.quit()

@pytest.fixture
def authenticated_driver(driver, base_url, valid_login_data):
  driver.get(base_url)
  login_page = LoginPage(driver)
  home_page = HomePage(driver)
  login_page.login(valid_login_data.get("username"), valid_login_data.get("password"))
  assert home_page.is_logged_in(), "Login failed in authenticated_driver fixture."
  return driver


@pytest.fixture(autouse=True, scope="session")
def configure_logging():
  os.makedirs("logs", exist_ok=True)
  log_filename = datetime.now().strftime("logs/test_run_%Y-%m-%d_%H-%M-%S.log")
  for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
  logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
      logging.FileHandler(log_filename)
    ]
  )

  logging.getLogger().setLevel(logging.DEBUG)


@pytest.fixture
def home_page(authenticated_driver):
  return HomePage(authenticated_driver)

@pytest.fixture
def cart_page(authenticated_driver):
  return CartPage(authenticated_driver)

@pytest.fixture
def product_page(authenticated_driver):
  return ProductPage(authenticated_driver)

@pytest.fixture
def checkout_step_one_page(authenticated_driver):
  return CheckoutStepOnePage(authenticated_driver)

@pytest.fixture
def checkout_step_two_page(authenticated_driver):
  return CheckoutStepTwoPage(authenticated_driver)

@pytest.fixture
def checkout_complete_page(authenticated_driver):
  return CheckoutCompletePage(authenticated_driver)

@pytest.fixture
def valid_login_data():
  return {
      "username": "standard_user",
      "password": "secret_sauce"
  }

@pytest.fixture(params=[
    {"username": "invalid_username", "password": "secret_sauce", "expected_result": "Epic sadface: Username and password do not match any user in this service"},
    {"username": "standard_user", "password": "invalid_password", "expected_result": "Epic sadface: Username and password do not match any user in this service"},
    {"username": "invalid_username", "password": "invalid_password", "expected_result": "Epic sadface: Username and password do not match any user in this service"}
])
def invalid_login_data(request):
    return request.param

@pytest.fixture(params=[
  {"username": "", "password": "secret_sauce", "expected_result": "Epic sadface: Username is required"},
  {"username": "standard_user", "password": "", "expected_result": "Epic sadface: Password is required"},
  {"username": "", "password": "", "expected_result": "Epic sadface: Username is required"}
])
def blank_login_data(request):
  return request.param

@pytest.fixture
def locked_out_user_data():
  return {
    "username": "locked_out_user",
    "password": "secret_sauce",
    "expected_result": "Epic sadface: Sorry, this user has been locked out."
  }

@pytest.fixture
def invalid_product_data():
  return {
      "name": "ITEM NOT FOUND",
      "description": "We're sorry, but your call could not be completed as dialled. Please check your number, and try your call again. If you are in need of assistance, please dial 0 to be connected with an operator. This is a recording. 4 T 1.",
      "price": "$√-1",
      "image": "https://www.saucedemo.com/static/media/sl-404.168b1cce.jpg"
  }

pages = [
    "inventory.html",
    "inventory-item.html",
    "cart.html",
    "checkout-step-one.html",
    "checkout-step-two.html",
    "checkout-complete.html"
]
@pytest.fixture(params=[{"page": p, "expected_result": f"Epic sadface: You can only access '/{p}' when you are logged in."} for p in pages])
def protected_pages(request):
    return request.param

@pytest.fixture
def valid_checkout_data():
  return {
      "first_name": "Mary",
      "last_name": "Anne",
      "postal_code": "90001"
  }


@pytest.fixture(params=[
    { "first_name": " ", "last_name": " ", "postal_code": " ", "expected_result": "Error..." },
    { "first_name": "@#$%&*!", "last_name": "@#$%&*!", "postal_code": "@#$%&*!", "expected_result": "Error..."},
    { "first_name": "123456789012345", "last_name": "123456789012345", "postal_code": "123456789012345", "expected_result": "Error..."},
    { "first_name": "🙂", "last_name": "🙈", "postal_code": "📍", "expected_result": "Error..."},
    { "first_name": "<script>alert('alert')</script>", "last_name": "<br>", "postal_code": "<h1>Attention!</h1>", "expected_result": "Error..."}
])
def invalid_checkout_data(request):
  return request.param

@pytest.fixture(params=[
      {"first_name": "", "last_name": "Anne", "postal_code": "90001", "expected_result": "Error: First Name is required"},
      {"first_name": "Mary", "last_name": "", "postal_code": "90001", "expected_result": "Error: Last Name is required"},
      {"first_name": "Mary", "last_name": "Anne", "postal_code": "", "expected_result": "Error: Postal Code is required"},
      {"first_name": "", "last_name": "", "postal_code": "", "expected_result": "Error: First Name is required"}
])
def blank_checkout_data(request):
  return request.param
