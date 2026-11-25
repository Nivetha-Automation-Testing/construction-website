from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
print("Title:", driver.title)
driver.save_screenshot("google_homepage.png")
time.sleep(5)
driver.quit()