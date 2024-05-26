from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re

# Define target Instagram hashtag
hashtag = "#newhollandtractor"

# Open a new Chrome browser window
driver = webdriver.Chrome()

# Go to Instagram login page
driver.get("https://www.instagram.com/accounts/login/")

# Login to your Instagram account
# Replace with your actual Instagram username and password
username = "your_username"
password = "your_password"

# Enter username and password in login fields
username_field = driver.find_element_by_name("username")
password_field = driver.find_element_by_name("password")
username_field.send_keys(username)
password_field.send_keys(password)

# Submit login form
login_button = driver.find_element_by_xpath("//button[@type='submit']")
login_button.click()

# Wait for the page to load completely
time.sleep(5)

# Search for the target hashtag
search_bar = driver.find_element_by_xpath("//input[@placeholder='Pesquisar']")
search_bar.send_keys(hashtag)
search_bar.send_keys(Keys.ENTER)

# Scroll down the search results page
last_position = driver.execute_script("return window.scrollY")
while True:
    new_position = driver.execute_script("return window.scrollY")
    if last_position == new_position:
        break
    last_position = new_position
    time.sleep(1)

# Extract leads from search results
leads = []
posts = driver.find_elements_by_xpath("//div[@class='v1NhDH']")
for post in posts:
    # Extract post content
    post_content = post.find_element_by_xpath(".//div[@class='C4VMk']").text

    # Check if post contains potential lead (phone number or email)
    if re.search(r"[0-9]{2,}-[0-9]{2,}-[0-9]{4,}", post_content) or re.search(r"[a-z0-9]+@[a-z]+\.[a-z]{2,3}", post_content):
        # Extract potential lead information
        potential_lead = re.search(r"[0-9]{2,}-[0-9]{2,}-[0-9]{4,}", post_content) or re.search(r"[a-z0-9]+@[a-z]+\.[a-z]{2,3}", post_content)
        lead = {
            "post_url": post.find_element_by_xpath(".//a[@href]").get_attribute("href"),
            "potential_lead": potential_lead.group(0)
        }
        leads.append(lead)

# Print captured leads
for lead in leads:
    print(f"Lead: {lead}")

# Close the browser window
driver.quit()
