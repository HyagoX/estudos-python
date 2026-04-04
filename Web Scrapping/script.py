import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

def scrape_website_data():
    # 1. Setup Chrome options for professional scraping
    chrome_options = Options()
    chrome_options.add_argument("--incognito")  # Open in incognito mode
    chrome_options.add_argument("--headless=new")  # Optional: run without opening window
    
    # 2. Initialize the WebDriver (Selenium Manager handles the driver automatically)
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        # Target URL (Example: Real Estate or E-commerce)
        url = "https://boletando.com/"
        driver.get(url)
        print(f"Connecting to: {url}")
        sleep(3)  # Initial wait for page load

        # 3. List to store extracted data
        extracted_results = []

        # 4. Find all item containers (Adjust XPath for specific site)
        items = driver.find_elements(By.XPATH, "//div[@class='product-card']")

        for item in items:
            try:
                # Extracting specific fields using relative XPaths
                title = item.find_element(By.XPATH, ".//h2").text
                price = item.find_element(By.XPATH, ".//span[@class='price']").text
                
                # Appending data to our list
                extracted_results.append({
                    "Product Name": title,
                    "Price": price
                })
            except Exception as e:
                continue # Skip items with missing data

        # 5. Exporting data to Excel/CSV using Pandas
        df = pd.DataFrame(extracted_results)
        df.to_csv("extracted_data.csv", index=False)
        print("Success! Data saved to extracted_data.csv")

    finally:
        # Close the browser session
        driver.quit()

if __name__ == "__main__":
    scrape_website_data()