import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestVisionpdf():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.driver.implicitly_wait(2000)  # Add implicit wait
        
    def teardown_method(self, method):
        self.driver.quit()
  
    def test_visionpdf(self):
        self.driver.get("https://visionias.in/resources/daily_current_affairs.php?type=1")
        self.driver.set_window_size(972, 816)
        self.driver.find_element(By.CSS_SELECTOR, ".small-12:nth-child(2) .dark-grey").click()
        self.driver.find_element(By.CSS_SELECTOR, ".col-sm-12:nth-child(1) .fa").click()
        self.driver.find_element(By.CSS_SELECTOR, "path:nth-child(2)").click()
        self.driver.find_element(By.ID, "pdf-1").click()

# Instantiate the test class and call the test method
test_instance = TestVisionpdf()
test_instance.setup_method(None)  # Call setup_method manually
test_instance.test_visionpdf()
