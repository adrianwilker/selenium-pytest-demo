
class TestShoppingCart:
  def test_remove_product_from_shopping_cart(self, home_page, cart_page):
    product_name = home_page.get_products()[0]["item_name"]
    home_page.add_to_shopping_cart(product_name)
    home_page.access_shopping_cart()
    cart_page.remove_product(product_name)
    assert not cart_page.product_exists(product_name)


  def test_values_in_the_shopping_cart(self, home_page, cart_page, checkout_step_one_page, checkout_step_two_page, valid_checkout_data):
    products = home_page.get_products()
    expected_subtotal = 0
    for p in products:
      home_page.add_to_shopping_cart(p["item_name"])
      expected_subtotal += p["item_price"]
    
    home_page.access_shopping_cart()
    cart_page.checkout()

    checkout_step_one_page.send_checkout_information(
      valid_checkout_data["first_name"], 
      valid_checkout_data["last_name"], 
      valid_checkout_data["postal_code"]
    )

    subtotal = checkout_step_two_page.get_subtotal()
    tax = checkout_step_two_page.get_tax()
    total = checkout_step_two_page.get_total()
    expected_total = expected_subtotal + tax

    assert expected_subtotal == subtotal, f"Subtotal expected to be {expected_subtotal}, but got {subtotal}"
    assert expected_total == total, f"Total expected to be {expected_total}, but got {total}"
