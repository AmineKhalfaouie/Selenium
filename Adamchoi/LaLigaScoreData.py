from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

# Set the website URL
website = "https://www.adamchoi.co.uk/overs/detailed"

# Create a Chrome webdriver
driver = webdriver.Chrome()

# Open the website
driver.get(website)

# Find and click the "All matches" button
all_matches_button = driver.find_element("xpath", "//label[@analytics-event='All matches']")
all_matches_button.click()

# Find the country dropdown and select 'Spain'
dropdown = Select(driver.find_element('id', 'country'))
dropdown.select_by_visible_text('Spain')

# Wait for a few seconds to allow the page to load
time.sleep(3)

# Find all matches (rows in the table) on the page
matches = driver.find_elements('tag name', 'tr')

# Create lists to store data
date = []
home_team = []
score = []
away_team = []

# Loop through each match and extract data
for match in matches:
    date.append(match.find_element('xpath', './td[1]').text)
    home = match.find_element('xpath', './td[2]').text
    home_team.append(home)
    score.append(match.find_element('xpath', './td[3]').text)
    away_team.append(match.find_element('xpath', './td[4]').text)

# Create a DataFrame from the collected data
df = pd.DataFrame({'date': date, 'home_team': home_team, 'score': score, 'away_team': away_team})

# Save the DataFrame to a CSV file
df.to_csv('football_data.csv', index=False)

# Print the DataFrame
print(df)
