from pages.home_page import HomePage
from pages.login_page import LoginPage

class TestAuthentication:
  
  def test_login_with_valid_credentials(self, driver, valid_login_data):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    login_page.login(valid_login_data.get("username"), valid_login_data.get("password"))
    assert home_page.is_logged_in(), "Login was not successful"


  def test_login_with_invalid_credentials(self, driver, invalid_login_data):
    login_page = LoginPage(driver)
    login_page.login(invalid_login_data["username"], invalid_login_data["password"])
    assert login_page.is_login_failed(invalid_login_data["expected_result"])
    

  def test_login_with_blank_fields(self, driver, blank_login_data):
    login_page = LoginPage(driver)
    login_page.login(blank_login_data["username"], blank_login_data["password"])
    assert login_page.is_login_failed(blank_login_data["expected_result"])


  def test_login_with_locked_out_user(self, driver, locked_out_user_data):
    login_page = LoginPage(driver)
    login_page.login(locked_out_user_data["username"], locked_out_user_data["password"])
    assert login_page.is_login_failed(locked_out_user_data["expected_result"])
    

  def test_access_protected_page_without_being_logged_in(self, driver, protected_pages, base_url):
    login_page = LoginPage(driver)
    login_page.access_page(base_url + protected_pages["page"])
    assert login_page.is_login_failed(protected_pages["expected_result"]), "Incorrect error message."
    assert login_page.get_current_url() == base_url, "Incorrect URL page."

  
  def test_logout(self, authenticated_driver, base_url):
    home_page = HomePage(authenticated_driver)
    home_page.open_menu()
    home_page.logout()
    current_url = home_page.get_current_url()
    assert current_url == base_url, f"Expected URL to be '{base_url}' but got '{current_url}'"
    assert not home_page.is_logged_in(), "User is logged in"