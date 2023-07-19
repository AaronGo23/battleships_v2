import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TestBattleships(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        
    def tearDown(self):
        self.driver.quit()
        
    def test_fill_history(self):
        driver = self.driver
        driver.get("https://web-application-6sve.onrender.com/")
        self.assertIn("Battleships", driver.title)
        self.assertIn("About Battleships", driver.page_source)
        fill_history_button = driver.find_element_by_link_text("Fill your last game's history")
        fill_history_button.click()
        name_field = driver.find_element_by_name("name1")
        name_field.send_keys("John")
        email_field = driver.find_element_by_name("name2")
        email_field.send_keys("Bob")
        message_field = driver.find_element_by_name("name_w")
        message_field.send_keys("Bob")
        message_field = driver.find_element_by_name("score")
        message_field.send_keys("850")
        submit_button = driver.find_element_by_xpath("//input[@type='submit']")
        submit_button.click()
        success_message = driver.find_element_by_xpath("//div[@class='alert alert-success']")
        self.assertIn("Your history has been submitted.", success_message.text)
        

if __name__ == "__main__":
    unittest.main()