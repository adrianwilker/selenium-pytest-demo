import pytest
from pages.home_page import SortType

class TestHomePage:
  
  @pytest.mark.parametrize("sort_type", [
    SortType.AZ,
    SortType.ZA,
    SortType.LOHI,
    SortType.HILO
  ])
  def test_reorder_product_list(self, sort_type, home_page):
    original_products = home_page.get_products()
    expected_order = home_page.sorted_products(original_products, sort_type)
    home_page.reorder_products(sort_type)
    reordered_products = home_page.get_products()
    reordered_products = home_page.remove_button_key_from_products(reordered_products)
    assert reordered_products == expected_order, "Products not reordered correctly."


  def test_add_product_to_shopping_cart_from_home_page(self, home_page, cart_page):
    product_name = home_page.get_products()[0]["item_name"]
    home_page.add_to_shopping_cart(product_name)
    home_page.access_shopping_cart()
    assert cart_page.product_exists(product_name), f"Product '{product_name}' not found in cart."
