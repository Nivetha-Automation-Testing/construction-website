from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 25)

driver.get("https://construction-ai-5at9.onrender.com/")

# =========================
#  TITLE
# =========================
title = driver.title
print("Website Title:", title)
assert title != ""

# =========================
#  SERVICES
# =========================
driver.find_element(By.LINK_TEXT, "Services").click()

services_text = wait.until(EC.visibility_of_element_located(
    (By.XPATH, "//h1 | //h2")
)).text

print("Services Page Navigated:", services_text)
assert services_text != ""

# =========================
# 🔹 PROJECTS
# =========================
driver.find_element(By.LINK_TEXT, "Projects").click()

projects_text = wait.until(EC.visibility_of_element_located(
    (By.XPATH, "//h1 | //h2")
)).text

print("Projects Page Navigated:", projects_text)
assert projects_text != ""

# =========================
#  ABOUT
# =========================
driver.find_element(By.LINK_TEXT, "About").click()

about_text = wait.until(EC.visibility_of_element_located(
    (By.XPATH, "//h1 | //h2")
)).text

print("About Page Navigated:", about_text)
assert about_text != ""

# =========================
#  CONTACT
# =========================
driver.find_element(By.LINK_TEXT, "Contact").click()

contact_text = wait.until(EC.visibility_of_element_located(
    (By.XPATH, "//h1 | //h2")
)).text

print("Contact Page Navigated:", contact_text)
assert contact_text != ""

# =========================
#  AI AGENT
# =========================
driver.find_element(By.ID, "aiAgentBtn").click()

chat_window = wait.until(EC.visibility_of_element_located((By.ID, "aiChatWindow")))
assert chat_window.is_displayed()
print("AI Agent Opened")

chat = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='aiChatWindow']//textarea")))
chat.send_keys("Tell me about your services")

send = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='aiChatWindow']//button")))
driver.execute_script("arguments[0].click();", send)

print("AI Message Sent")

time.sleep(2)
driver.find_element(By.ID, "aiAgentBtn").click()
print("AI Agent Closed")

# =========================
#  FREE CONSULTATION
# =========================
driver.find_element(By.CLASS_NAME, "btn-consultation").click()

name = wait.until(EC.visibility_of_element_located((By.NAME, "name")))
print("Form Opened")
assert name.is_displayed()

# =========================
#  FORM FILL
# =========================
name.send_keys("Shine")
driver.find_element(By.NAME, "email").send_keys("shine@gmail.com")
driver.find_element(By.NAME, "phone").send_keys("9876543210")

print("Basic Details Entered")

dropdown = Select(wait.until(EC.presence_of_element_located((By.ID, "id_project_type"))))
dropdown.select_by_visible_text("Residential")

selected = dropdown.first_selected_option.text
print("Dropdown Selected:", selected)
assert selected != ""

driver.find_element(By.NAME, "message").send_keys("Automation Testing")
print("Message Entered")

# =========================
#  SUBMIT
# =========================
submit = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
driver.execute_script("arguments[0].click();", submit)

print("Form Submitted")

# =========================
#  FINAL SUCCESS MESSAGE
# =========================
success = wait.until(EC.visibility_of_element_located((
    By.XPATH, "//*[contains(text(),'Thank you')]"
)))

final_message = success.text

print("Final Message:", final_message)

assert final_message != ""
assert "Thank" in final_message

# =========================
# END
# =========================
time.sleep(5)
driver.quit()