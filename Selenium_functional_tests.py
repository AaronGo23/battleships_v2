from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Instantiate a Chrome browser
driver = webdriver.Chrome()

# Navigate to the home page
driver.get("https://web-application-6sve.onrender.com/")

# Check that the home page contains the expected text
assert "Battleships" in driver.title
assert "About Battleships" in driver.page_source

# Click on the "Fill your last game's history" button
fill_history_button = driver.find_element_by_link_text("Fill your last game's history")
fill_history_button.click()

# Fill out the history form and submit it
name1_field = driver.find_element_by_name("name1")
name1_field.send_keys("John")
name2_field = driver.find_element_by_name("name2")
name2_field.send_keys("Bob")
namew_field = driver.find_element_by_name("name_w")
namew_field.send_keys("Bob")
w_score_field = driver.find_element_by_name("score")
w_score_field.send_keys("850")
submit_button = driver.find_element_by_xpath("//input[@type='submit']")
submit_button.click()

# Check that the success message is displayed
success_message = driver.find_element_by_xpath("//div[@class='alert alert-success']")
assert "Your history has been submitted." in success_message.text


# Close the browser
driver.quit()