import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

class POSAdminTestCase(unittest.TestCase):

    def setUp(self):
        # Create a Chrome webdriver with the help of webdriver_manager
 driver = webdriver.Chrome(ChromeDriverManager().install())

# Now you can use the 'driver' object to automate the browser
driver.get("https://qadir.asoftpos.com/en/admin/login")

    def tearDown(self):
        # Clean up after the test case is executed
        self.driver.quit()

    def test_login_to_admin_panel(self):
        # Open the POS admin panel login page
        self.driver.get("https://qadir.asoftpos.com/en/admin/login")

        # Assert that the login page is loaded successfully
        #self.assertEqual("ASoftPOS - Login", self.driver.title)

        # Enter the username and password
        username_input = self.driver.find_element_by_name("email")
        username_input.send_keys("gq2853248@gmail.com")
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys("12345678")

        # Submit the login form
        password_input.send_keys(Keys.RETURN)

        # Assert that the admin panel page is loaded after successful login
        self.assertEqual("ASoftPOS - Admin Panel", self.driver.title)

    def test_add_product(self):
        # Log in to the admin panel
        self.test_login_to_admin_panel()

        # Open the "Products" page
        self.driver.get("https://qadir.asoftpos.com/en/admin/products")

        # Assert that the "Products" page is loaded successfully
        self.assertEqual("ASoftPOS - Products", self.driver.title)

        # Click on the "Add New Product" button
        add_product_button = self.driver.find_element_by_xpath("//button[contains(text(), 'Add New Product')]")
        add_product_button.click()

        # Assert that the "Add New Product" page is loaded
        self.assertEqual("ASoftPOS - Add New Product", self.driver.title)

        # Fill in the product details
        product_name_input = self.driver.find_element_by_name("name")
        product_name_input.send_keys("New Product")
        product_price_input = self.driver.find_element_by_name("price")
        product_price_input.send_keys("9.99")
        # Add more fields as per your application's requirements

        # Submit the product form
        submit_button = self.driver.find_element_by_xpath("//button[contains(text(), 'Submit')]")
        submit_button.click()

        # Assert that the product is added successfully
        success_message = self.driver.find_element_by_class_name("alert-success").text
        self.assertEqual("Product added successfully.", success_message)

if __name__ == "__main__":
    unittest.main()
