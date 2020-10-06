# Generated by Selenium IDE
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


class TestMm():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_mm(self):
        self.driver.get("http://localhost:9999/statements")
        self.driver.set_window_size(1292, 766)
        self.driver.find_element(By.CSS_SELECTOR, ".container > .container").click()
        self.driver.find_element(By.CSS_SELECTOR, ".container:nth-child(3)").click()
        self.driver.find_element(By.LINK_TEXT, "2").click()
        self.driver.find_element(By.CSS_SELECTOR, ".disabled > .page-link").click()
        self.driver.find_element(By.CSS_SELECTOR, "body").click()
        self.driver.find_element(By.CSS_SELECTOR, "#statement_row_5 > #date").click()
        self.driver.find_element(By.CSS_SELECTOR, ".col-sm").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()


obj = TestMm()
obj.setup_method('')
obj.test_mm()
# obj.teardown_method('')