
## Test Cases
|   ID   | Functionality | Precondition |   Steps   | Expected result | Status |
| ------ | ------------- | ------------ | --------- | --------------- | ------ |
| CT01 | Valid login | Be on the login page  | 1. Enter a valid username <br> 2. Enter a valid password for the user <br> 3. Click the 'Login' button | Log in successfully; get to the product page ('*/inventory.html*') | Passed |
| CT02 | Login with invalid password | Be on the login page  | 1. Enter a valid username <br> 2. Enter a invalid password for the user <br> 3. Click the 'Login' button | Show message *"Epic sadface: You can only access '/inventory.html' when you are logged in."* | Passed |
| CT03 | Add products to shopping cart from details page | Be logged in and on the home page | 1. Identify the product you want and click on its "add to cart" button <br> 2. Access the shopping cart through the icon in the upper right corner | The added product should be displayed on the page. | Passed
| CT04 | Buy one product | Having one product in the shopping cart | 1. Access the shopping cart <br> 2. Click the 'checkout' button <br> 2. Fill in the first name, last name and zip/postal code fields <br> 3. Click the 'continue' button <br> 4. Confirm the purchase details on the Overview page <br> 5. Click the 'finish' button | The checkout complete page should be displayed, with the message *"Thank you for your order!"* | Passed
| CT05 | Buy two products | Having two products in the shopping cart | 1. Access the shopping cart <br> 2. Click the 'checkout' button <br> 2. Fill in the first name, last name and zip/postal code fields <br> 3. Click the 'continue' button <br> 4. Confirm the purchase details on the Overview page <br> 5. Click the 'finish' button | The checkout complete page should be displayed, with the message *"Thank you for your order!"* | Passed
| CT06 | Remove product from shopping cart | Have at least one product in the shopping cart | 1. Access the shopping cart <br> 2. Click on "Remove" next to the chosen product | The product should no longer be displayed on the shopping cart page | Passed
| CT07 | Login with blank fields | Be on the login page | 1. Fill in only the username field or only the password field or neither <br> 2. Click the 'Login' button | Show message *"Epic sadface: <Username/Password> is required"* | Passed |
| CT08 | Login with locked out user | Be on the login page | 1. Fill in the first field with a username that is blocked <br> 2. Fill in the second field with the password linked to the username <br> 3. Click the 'Login' button | Show message *"Epic sadface: Sorry, this user has been locked out."* | Passed |
| CT09 | Logout | Be logged in and on the home page | 1. Click on the icon in the upper left corner to open the menu <br> 2. Click 'logout' | Log out successfully; be taken to the login page. | Passed |
| CT10 | Checkout with blank fields | Have at least one product in the shopping cart | 1. Access the shopping cart through the icon in the upper right corner <br> 2. Click the 'checkout' button <br> 3. Leave the 'first name' or 'last name' or 'postal code' field blank or all of them <br> 4. Click the 'continue' button <br> An error message should appear informing that the field is required. | Passed |
| CT11 | Checkout with empty shopping cart | The user must be logged in; there must be no products in the shopping cart | 1. Access the shopping cart <br> 2. Click the 'checkout' button | The user must remain on the current page, prevented from proceeding with the checkout process. | Failed |
| CT12 | Reorder product list | The user must be logged in and on the home page. | 1. Click on the filter option in the top right corner <br> 2. Select one of the options from the dropdown menu: Name (A to Z), Name (Z to A), Price (low to high) or Price (high to low) | The product listing must be ordered according to the selected option. | Passed |
| CT13 | Add product to shopping cart from home page | The user must be logged in and on the home page | 1. Locate the desired product and click on its "add to cart" button <br> 2. Access the shopping cart | The product must be in the shopping cart. | Passed |
| CT14 | Access protected page without being logged in | The user must not be logged in | 1. Try to access a protected page directly via the URL | The login page should be displayed; a message should indicate that the page the user tried to access is only possible when logged in. | Passed |
| CT15 | Access the page of nonexistent product | The user must be logged in | 1. Insert the id of a non-existent product in the url | The system should indicate that the product was not found | Passed |
| CT16 | Add invalid product to shopping cart | The user must not be logged in | 1. Insert the id of a non-existent product in the url <br> 2. Click the 'Add to cart' button <br> 3. Access the shopping cart page | No products should be displayed on the shopping cart page, but it should load successfully. | Failed |
| CT17 | Values in the shopping cart | The user must not be logged in | 1. Add at least two products to the shopping cart <br> 2. Access the shopping cart page <br> 3. Click the 'checkout' button <br> 4. Fill in the fields 'first name', 'last name' and 'postal code' and click 'continue' | The 'item total', 'tax' and 'total' values ​​must be calculated correctly. | Passed |
| CT18 | Checkout with invalid data | Have at least one product in the shopping cart | 1. Access the shopping cart <br> 2. Click the 'checkout' button <br> 3. Fill in the fields 'first name', 'last name' and 'postal code' with invalid values <br> 4. Click 'continue' | The system should display an error message. | Failed |

## 🐞 Bug Report
|||
|-|-|
| **Title:** | System allows user to complete checkout without having items in cart.  |
| **ID:** | BUG01  
| **Test Case ID:** | CT11
| **Priority:** | High  
| **Severity:** | Critical  
| **Description:** | The system allows users to complete the purchase process even without adding items to the shopping cart. After completing the checkout information, the user is redirected to the confirmation screen with the message "Thank you for your order!"  This behavior can lead to invalid or inconsistent order records.
| **Steps to reproduce** | 1. Log in with valid credentials <br> 2. Do not add any items to the cart <br> 3. Click the cart icon (which is empty) <br> 4. Click the Checkout button <br> 5. Fill in the shipping information (First Name, Last Name, Zip/Postal Code) <br> 6. Continue to checkout.
| **Current Result** | The system allows you to complete the purchase and displays the confirmation message: "Thank you for your order!"
| **Expected Result** | The system should prevent the user from starting or completing checkout without items in the cart by displaying an error message or disabling the action.
| **Evidence** | <inserir gif>

---

|||
|-|-|
| **Title:** | System allows user to add invalid product to shopping cart  |
| **ID:** | BUG02  
| **Test Case ID:** | CT16
| **Priority:** | High  
| **Severity:** | Critical  
| **Description:** | The system has a fictitious product with the title "product not found" that is displayed when the page of a non-existent product is accessed. This product has a button that allows the user to add it to the shopping cart. When it's added, the cart becomes inaccessible.
| **Steps to reproduce** | 1. Log in with valid credentials <br> 2. Do not add any items to the cart <br> 3. Access the page of an invalid product, inserting a non-existent id at the end of the url '/inventory-item.html?id=' <br> 4. Click the 'add to cart' button <br> 5. Access the shopping cart by clicking on the icon in the upper right corner.
| **Current Result** | The shopping cart page does not load.
| **Expected Result** | The 'add to cart' button for the fictitious product should be disabled or non-existent.
| **Evidence** | <inserir gif>

---

|||
|-|-|
| **Title:** | The system allows the user to checkout with invalid data  |
| **ID:** | BUG03  
| **Test Case ID:** | CT18
| **Priority:** | High  
| **Severity:** | Critical  
| **Description:** | During checkout, the first name, last name, and postal code fields accept invalid values ​​such as special characters, white space, and numbers.
| **Steps to reproduce** | 1. Log in with valid credentials <br> 2. Add a product to the shopping cart <br> 3. Access the shopping cart <br> 4. Click the 'checkout' button <br> 5. Fill in the 'first name' and 'last name' fields with invalid values ​​(numbers, emojis, special characters and blank spaces) 6. Fill in the 'postal code' field with invalid values (emojis, special characters and blank spaces) <br> 7. Click 'continue'
| **Current Result** | The user is taken to the Overview screen.
| **Expected Result** | The user should stay on the current screen and an appropriate error message should be displayed, informing that the data entered is not allowed.
| **Evidence** | <inserir gif>