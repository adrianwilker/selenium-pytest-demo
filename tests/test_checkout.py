import pytest
import logging

class TestCheckout:

  @pytest.mark.xfail(reason="Bug: the system should not accept invalid data in the checkout fields.")
  def test_checkout_with_invalid_data(self, home_page, cart_page, checkout_step_one_page, invalid_checkout_data):
    product_name = home_page.get_products()[5]["item_name"]
    home_page.add_to_shopping_cart(product_name)
    home_page.access_shopping_cart()
    cart_page.checkout()
    checkout_step_one_page.send_checkout_information(invalid_checkout_data["first_name"], invalid_checkout_data["last_name"], invalid_checkout_data["postal_code"])
    logging.warning("The system allow to complete checkout with invalid data")
    assert '/checkout-step-one.html' in checkout_step_one_page.get_current_url(), "The checkout worked when it shouldn't have."


  def test_checkout_with_blank_fields(self, home_page, cart_page, checkout_step_one_page, blank_checkout_data):
    product_name = home_page.get_products()[3]["item_name"]
    home_page.add_to_shopping_cart(product_name)
    home_page.access_shopping_cart()
    cart_page.checkout()
    checkout_step_one_page.send_checkout_information(blank_checkout_data["first_name"], blank_checkout_data["last_name"], blank_checkout_data["postal_code"])
    assert checkout_step_one_page.check_error_message_text() == blank_checkout_data["expected_result"], "The checkout worked when it shouldn't have."


  @pytest.mark.xfail(reason="Bug: The system should not allow checkout completion when there are no products in the shopping cart.")
  def test_checkout_with_empty_shopping_cart(self, home_page, cart_page, checkout_step_one_page, valid_checkout_data, checkout_step_two_page, checkout_complete_page):
    home_page.access_shopping_cart()
    cart_page.checkout()
    checkout_step_one_page.send_checkout_information(valid_checkout_data["first_name"], valid_checkout_data["last_name"], valid_checkout_data["postal_code"])
    checkout_step_two_page.finish()
    logging.warning("The system allow to complete checkout without items in the cart")
    assert checkout_complete_page.not_exists(checkout_complete_page.success_message), "The checkout worked when it shouldn't have."
