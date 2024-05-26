from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Define the target Twitter search term
search_term = "#leadgeneration"

# Open a new Chrome browser window
driver = webdriver.Chrome()

# Go to Twitter homepage
driver.get("https://twitter.com/?lang=en")

# Login to your Twitter account
# Replace with your actual Twitter username and password
username = "your_username"
password = "your_password"

# Enter username and password in login fields
username_field = driver.find_element_by_name("session[username_or_email]")
password_field = driver.find_element_by_name("session[password]")
username_field.send_keys(username)
password_field.send_keys(password)

# Submit login form
login_button = driver.find_element_by_xpath("//button[@type='submit']")
login_button.click()

# Search for the target term
search_bar = driver.find_element_by_xpath("//input[@data-testid='search-box']")
search_bar.send_keys(search_term)
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
tweets = driver.find_elements_by_xpath("//div[@data-testid='tweet']")
for tweet in tweets:
    # Extract tweet content
    tweet_content = tweet.find_element_by_xpath(".//div[@data-testid='tweetText']").text

    # Extract user profile information
    user_info = tweet.find_element_by_xpath(".//div[@data-testid='tweetHeader']")
    username = user_info.find_element_by_xpath(".//a[@data-testid='link']").text
    profile_url = user_info.find_element_by_xpath(".//a[@data-testid='link']").get_attribute("href")

    # Check if tweet contains a potential lead
    if any(word in tweet_content for word in ["contact", "inquire", "business"]):
        lead = {
            "username": username,
            "profile_url": profile_url,
            "tweet_content": tweet_content
        }
        leads.append(lead)

# Print captured leads
for lead in leads:
    print(f"Lead: {lead}")

# Close the browser window
driver.quit()
