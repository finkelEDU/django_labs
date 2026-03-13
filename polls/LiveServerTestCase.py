from django.test import LiveServerTestCase
#from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver

#LiveServerTestCase
class LiveServerTestCase(LiveServerTestCase):
    fixtures = ["user-data.json"]
    
    @classmethod
    def setUpClass(cls):
        super.setupClass()
        cls.selenium = WebDriver
    
    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()
        
        def test_login(self):
            self.selenium.get(f"{self.live_server_url}/login/")
            username_input = self.selenium.find_element(By.NAME, "username")
            username_input.send_keys("myuser")
            password_input = self.selenium.find_element(By.NAME, "password")
            password_input.send_keys("secret")
            self.selenium.find_element(By.XPATH, '//input[@value="Log in"]').click()