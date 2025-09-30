# Automated UI Tests for SauceDemo
![image](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![image](https://img.shields.io/badge/Selenium-00B400?style=for-the-badge&logo=selenium&logoColor=white)
![image](https://img.shields.io/badge/Pytest-049DD9?style=for-the-badge&logo=pytest&logoColor=white)

This project contains automated tests of the **SauceDemo** application using **Selenium** and **Pytest**. It simulates user interactions such as adding products to the cart, completing checkout, and verifying product reordering.

[Test cases](https://github.com/adrianwilker/selenium-pytest-demo/blob/main/TEST_CASES.md#test-cases) and [bug reports](https://github.com/adrianwilker/selenium-pytest-demo/blob/main/TEST_CASES.md#-bug-report) are documented in the [TEST_CASES.md](https://github.com/adrianwilker/selenium-pytest-demo/blob/main/TEST_CASES.md) file.

## Technologies

- Python 3.11+
- Selenium
- Pytest
- GitHub Actions (CI/CD)
- ChromeDriver

## Prerequisites

- Python 3.11 or higher
- Chrome Browser
- ChromeDriver

## Installation

```bash
git clone <REPO_URL>
cd <REPO_NAME>
python -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate.ps1      # Windows
pip install -r requirements.txt
```

## Running tests
- All tests:
```bash
pytest
```

- Specific tests:
```bash
pytest ./tests/test_home_page.py::CLASS_NAME::FUNCTION_NAME
```

## Project structure

```bash
project/
├─ pages/                 # Page Objects
│  ├─ base_page.py
│  ├─ login_page.py
│  ├─ home_page.py
│  ├─ product_page.py
│  ├─ cart_page.py
│  ├─ checkout_step_one_page.py
│  ├─ checkout_step_two_page.py
│  └─ checkout_complete_page.py
├─ tests/                 # Test cases
│  ├─ test_authentication.py
│  ├─ test_home_page.py
│  ├─ test_product_page.py
│  ├─ test_shopping_cart.py
│  ├─ test_checkout.py
│  └─ test_purchase_flow.py
├─ conftest.py
├─ pytest.ini
├─ requirements.txt
└─ .github/workflows/tests.yml
```

## CI/CD Integration

Tests are automatically run by GitHub Actions whenever there's a push or pull request in the repository.

## Notes

- Tests marked with ```@pytest.mark.xfail``` indicate known bugs.

- Make sure the Selenium driver is compatible with your browser.

