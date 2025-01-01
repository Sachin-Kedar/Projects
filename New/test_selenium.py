from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up WebDriver for Chromium
driver = webdriver.Chrome()

# Open a webpage
driver.get("https://example.com")

# Interact with an input box
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Automation testing with Python" + Keys.RETURN)

# Close the browser
driver.quit()
