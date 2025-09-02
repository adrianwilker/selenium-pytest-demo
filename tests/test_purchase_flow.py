
class TestPurchaseFlow:
  def test_buy_one_product(self, home_page, cart_page, checkout_step_one_page, checkout_step_two_page, checkout_complete_page, valid_checkout_data):
    product_name = home_page.get_products()[0]["item_name"]
    home_page.add_to_shopping_cart(product_name)
    home_page.access_shopping_cart()
    assert cart_page.product_exists(product_name), f"The product '{product_name}' is not in the shopping cart."
    cart_page.checkout()
    checkout_step_one_page.send_checkout_information(valid_checkout_data["first_name"], valid_checkout_data["last_name"], valid_checkout_data["postal_code"])
    checkout_step_two_page.finish()
    assert checkout_complete_page.is_checkout_successful(), "Checkout error"


  def test_buy_two_products(self, home_page, cart_page, checkout_step_one_page, checkout_step_two_page, checkout_complete_page, valid_checkout_data):
    product1_name = home_page.get_products()[0]["item_name"]
    product2_name = home_page.get_products()[1]["item_name"]
    home_page.add_to_shopping_cart(product1_name)
    home_page.access_shopping_cart()
    assert cart_page.product_exists(product1_name), f"The product '{product1_name}' is not in the shopping cart."
    cart_page.click_continue_shopping()
    home_page.add_to_shopping_cart(product2_name)
    home_page.access_shopping_cart()
    assert cart_page.product_exists(product2_name), f"The product '{product2_name}' is not in the shopping cart."
    cart_page.checkout()
    checkout_step_one_page.send_checkout_information(valid_checkout_data["first_name"], valid_checkout_data["last_name"], valid_checkout_data["postal_code"])
    checkout_step_two_page.finish()
    assert checkout_complete_page.is_checkout_successful(), "Checkout error"

