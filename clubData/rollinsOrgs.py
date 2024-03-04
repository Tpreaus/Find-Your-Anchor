from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import os
import csv

# Specify the path to your WebDriver using a relative path
s = Service(os.path.join(os.path.dirname(__file__), 'drivers', 'chromedriver'))

# Initialize the WebDriver with the Service object
driver = webdriver.Chrome(service=s)

driver.get('https://getinvolved.rollins.edu/organizations')

# Click the "Load More" button repeatedly until all activities are loaded
while True:
    try:
        load_more_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='button'] span"))
        )
        # Scroll to the button
        driver.execute_script("arguments[0].scrollIntoView();", load_more_button)
        # Wait for the overlapped element to disappear
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".loading-spinner")))
        # Click the button using JavaScript
        driver.execute_script("arguments[0].click();", load_more_button)
        # Wait for the new activities to load
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".loading-spinner")))
        # Re-locate the "Load More" button to ensure it's up-to-date
        load_more_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='button'] span"))
        )
        # Check if the "Load More" button is disabled or not visible
        if not load_more_button.is_enabled() or not load_more_button.is_displayed():
            break  # Exit the loop if there are no more activities to load
    except (NoSuchElementException, StaleElementReferenceException):
        # If the "Load More" button is not found or stale, all activities have been loaded
        break

# Scrape activity names and descriptions
activities = driver.find_elements(By.CSS_SELECTOR, "div[style*='font-weight: 600']")
descriptions = driver.find_elements(By.CSS_SELECTOR, "p.DescriptionExcerpt")

# Prepare data to be written into the CSV file
data_to_write = []
for activity, description in zip(activities, descriptions):
    data_to_write.append([activity.text, description.text])

# Write the scraped data to a CSV file
csv_file_path = 'rollins_activities_and_descriptions.csv'
try:
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Activity Name', 'Description'])  # Writing the header
        writer.writerows(data_to_write)
    print("Data successfully written to CSV file:", csv_file_path)
except Exception as e:
    print("Error writing data to CSV file:", e)

# Close the driver
driver.quit()
