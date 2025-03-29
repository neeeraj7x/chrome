import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Configuration
WEBSITE_URL = "https://ipl2025allupdatein.blogspot.com/2025/03/rcb-vs-csk-royal-challengers-bengaluru.html"  # Change to your target website
WAIT_TIME = 15  # Seconds between reloads
CLICK_X = 100   # X coordinate to click
CLICK_Y = 100   # Y coordinate to click

def setup_driver():
    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--start-maximized")
    
    # Automatic driver management
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def main():
    while True:
        try:
            print("Starting new session...")
            driver = setup_driver()
            
            # Open website
            driver.get(WEBSITE_URL)
            print(f"Opened: {WEBSITE_URL}")
            
            # Perform click
            action = ActionChains(driver)
            action.move_by_offset(CLICK_X, CLICK_Y).click().perform()
            print(f"Clicked at ({CLICK_X}, {CLICK_Y})")
            
            # Wait and reload
            print(f"Waiting {WAIT_TIME} seconds...")
            time.sleep(WAIT_TIME)
            
            # Clean up
            driver.quit()
            print("Session ended. Restarting...\n")
            
        except Exception as e:
            print(f"Error occurred: {str(e)}")
            if 'driver' in locals():
                driver.quit()
            time.sleep(5)  # Wait before retrying

if __name__ == "__main__":
    main()
