import pytest

class TestProductPage:

  def test_access_the_page_of_nonexistent_product(self, product_page, base_url, invalid_product_data):
    invalid_id = "-1"
    product_page.access_page(base_url + "inventory-item.html?id=" + invalid_id)
    product = product_page.get_product_info()
    for key, expected_value in invalid_product_data.items():
      assert product[key] == expected_value, (
        f"Expected {key}='{expected_value}', but got '{product[key]}'"
      )


  def test_add_product_to_shopping_cart_from_product_page(self, home_page, product_page, cart_page):
    product_name = home_page.get_products()[0]["item_name"]
    home_page.access_product_page(product_name)
    product_page.add_to_shopping_cart()
    product_page.access_shopping_cart()
    assert cart_page.product_exists(product_name)


  @pytest.mark.xfail(reason="Bug: non-existent product can be added to shopping cart, and shopping cart page does not load.")
  def test_add_invalid_product_to_shopping_cart(self, base_url, product_page):
    invalid_id = "-1"
    product_page.access_page(base_url + "inventory-item.html?id=" + invalid_id)
    product = product_page.get_product_info()
    assert not product_page.find_element(product["button"]).is_enabled(), "the 'add to cart' button is enabled"


