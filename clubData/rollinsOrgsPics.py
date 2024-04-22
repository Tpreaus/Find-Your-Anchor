from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException
import csv
import os

chromedriver_path = '/Users/philipclarke/Find-Your-Anchor/drivers/chromedriver'
s = Service(chromedriver_path)
driver = webdriver.Chrome(service=s)
driver.get('https://getinvolved.rollins.edu/organizations')

try:
    load_more_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='button'] span"))
    )
    ActionChains(driver).move_to_element(load_more_button).perform()
    load_more_button.click()
    WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".loading-spinner")))
except TimeoutException:
    print("Initial button click failed.")
    driver.save_screenshot('debug_screenshot.png')

def safe_click(button_selector):
    try:
        # Attempt to find the button and click it.
        button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, button_selector))
        )
        driver.execute_script("arguments[0].scrollIntoView();", button)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, button_selector))
        )
        button.click()
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".loading-spinner")))
        return True
    except ElementClickInterceptedException:
        # If other elements are blocking, use JavaScript click as fallback.
        driver.execute_script("arguments[0].click();", button)
        return True
    except StaleElementReferenceException:
        # If element goes stale, try re-acquiring the element.
        return safe_click(button_selector)
    except TimeoutException:
        # If the button doesn't appear within the timeout, assume it might be gone and check again.
        try:
            # Double-check the presence of the button to avoid false positives due to timing issues.
            driver.find_element(By.CSS_SELECTOR, button_selector)
            return True  # The button is still there, but wasn't clickable in time.
        except NoSuchElementException:
            # Button is truly gone.
            return False
    except NoSuchElementException:
        # If the button is no longer present, return False.
        return False

# Usage in the main script loop
while True:
    if not safe_click("button[type='button'] span"):
        print("No more 'Load More' buttons to press or failed to click. Ending pagination.")
        break

# Scrape activity names, descriptions, and image URLs
activities = driver.find_elements(By.CSS_SELECTOR, "div[style*='font-weight: 600']")
descriptions = driver.find_elements(By.CSS_SELECTOR, "p.DescriptionExcerpt")
images = driver.find_elements(By.CSS_SELECTOR, "img")

data_to_write = []
for activity, description, image in zip(activities, descriptions, images):
    data_to_write.append([activity.text, description.text, image.get_attribute('src')])

csv_file_dir = 'clubData'
csv_file_path = os.path.join(csv_file_dir, 'rollins_activities_descriptions_images.csv')

try:
    # Ensure the directory exists
    if not os.path.exists(csv_file_dir):
        os.makedirs(csv_file_dir)

    with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Activity Name', 'Description', 'Image URL'])
        writer.writerows(data_to_write)
    print("Data successfully written to CSV file:", csv_file_path)
except Exception as e:
    print("Error writing data to CSV file:", e)

driver.quit()
