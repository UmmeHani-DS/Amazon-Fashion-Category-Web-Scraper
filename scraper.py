#!/usr/bin/env python
# coding: utf-8

# # AMAZON MEN'S ACCESSORIES SCRAPER

# In[72]:


import re
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from bs4 import BeautifulSoup
import time
import json


# In[40]:


# Function to load proxies from file (optional)
def load_proxies(filename):
    with open(filename) as f:
        proxies = f.read().splitlines()
    return proxies

# Function to set up Selenium WebDriver with a random proxy (optional)
def setup_driver_with_proxy(proxies):
    options = webdriver.FirefoxOptions()
    if proxies:  # Use proxy if available
        proxy_address = random.choice(proxies)
        options.add_argument('--proxy-server=%s' % proxy_address)
    driver = webdriver.Firefox(options=options)
    return driver

# Load proxies from file (optional)
proxies = load_proxies(r"proxies.txt")

# Replace with the actual URL of the page you want to scrape
url = "https://www.amazon.com/s?i=fashion-mens-intl-ship&bbn=16225019011&rh=n%3A7141123011%2Cn%3A16225019011%2Cn%3A2474937011&page=2&qid=1708486826&ref=sr_pg_1"

# Create an empty set to store unique links
unique_product_links = set()

# Number of pages to scrape (adjust as needed)
max_pages = 500

# Page counter
page_count = 0

# Set up WebDriver (use proxy if desired)
driver = setup_driver_with_proxy(proxies)  # Uncomment if using proxies

# Navigate to the initial page
driver.get(url)

while page_count < max_pages:
    try:
        # Wait for page to load (adjust timeout as needed)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search")))

        # Get initial page height
        last_height = driver.execute_script("return document.documentElement.scrollHeight")

        # Scroll down gradually with small pauses
        while True:
            # Scroll down a portion of the page height
            scroll_down_amount = int(last_height * 0.3)  # Adjust scroll amount as needed
            driver.execute_script(f"window.scrollTo(0, window.scrollY + {scroll_down_amount})")

            # Wait for content to load after scrolling
            time.sleep(1)

            # Get new page height
            new_height = driver.execute_script("return document.documentElement.scrollHeight")

            # Check if scrolling has reached the bottom
            if new_height == last_height:
                break

            last_height = new_height

        # Parse HTML content
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')

        # Find product links on the current page
        product_links_on_page = [f"https://www.amazon.com/{a['href']}" for a in soup.find_all('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')]

        # Extract links and filter duplicates using set membership
        unique_links_on_page = [link for link in product_links_on_page if link not in unique_product_links]

        # Add unique links to the main list
        unique_product_links.update(unique_links_on_page)

        # Check for next button
        next_button = driver.find_elements(By.XPATH, "//*[@id='search']/div[1]/div[1]/div/span[1]/div[1]/div[62]/div/div/span/a[4]")

        if next_button:
            # Simulate human-like delay before clicking (adjust as needed)
            time.sleep(random.uniform(3, 6))

            # Click the next button
            next_button[0].click()
            page_count += 1  # Increment counter after successful page transition
        else:
          # No more pages or limit reached, break the loop
            break
    except NoSuchElementException:
        # Handle cases where the next button is not found or other exceptions occur
        print("Next button not found or other error occurred. Stopping scraping.")
        break


        
driver.quit()


# In[41]:


for idx, links in enumerate(unique_product_links):
        print(f"link {idx + 1} : {links}")
        print("\n")


# In[70]:


# Set up WebDriver (use proxy if desired)
driver = setup_driver_with_proxy(proxies)  # Uncomment if using proxies

# Convert the set to a list
unique_product_links_list = list(unique_product_links)

# Iterate through the first link in the list
for product_url in unique_product_links_list[:1]: 
    
    try:
        # Navigate to the product page
        driver.get(product_url)

        # Wait for page to load (adjust timeout as needed)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "productTitle")))

        # Get page source
        page_source = driver.page_source

        # Parse HTML content
        soup = BeautifulSoup(page_source, 'html.parser')

        # Extract product details 
        
        product_name = soup.find("span", id="productTitle").text.strip() 

        # Extract product description
        description = soup.find("div", id="productDescription").text.strip()
        
        # Find the span containing the price information
        price_span = soup.find('span', class_='aok-offscreen')

        # If the span is found, extract the text and strip any whitespace
        if price_span:
            price = price_span.text.strip()
        else:
            print("Price information not found.")
         
         # Extract the ASIN i.e product ID
        
        asin_element = driver.find_element(By.CSS_SELECTOR, '#detailBullets_feature_div > ul > li:nth-child(5) > span > span:nth-child(2)')
        product_id = asin_element.text.strip()
         
        # Extract the brand Name
        
        brand_element = driver.find_element(By.CSS_SELECTOR, '#detailBullets_feature_div > ul > li:nth-child(4) > span > span:nth-child(2)')
        brand_name = brand_element.text.strip()
        
        # Extract Category
        
        # Category
        b_element = driver.find_element(By.CSS_SELECTOR, '#wayfinding-breadcrumbs_feature_div > ul > li:nth-child(5) > span > a')
        category = b_element.text.strip()

        # Sub-category
        c_element = driver.find_element(By.CSS_SELECTOR, '#wayfinding-breadcrumbs_feature_div > ul > li:nth-child(7) > span > a')
        sub_category = c_element.text.strip()
        
        # Extract Gender
        
        g_element = driver.find_element(By.CSS_SELECTOR, '#wayfinding-breadcrumbs_feature_div > ul > li:nth-child(3) > span > a')
        gender = g_element.text.strip()
        
        

        # Extract product reviews (replace with desired review scraping logic)
        # Replace this placeholder with your implementation to scrape reviews and rankings
        product_reviews = []

        # Print extracted details
        print(f"Product URL: {product_url}")
        print(f"Category: {category}")
        print(f"Sub Category: {sub_category}")
        print(f"Brand Name: {brand_name}")
        print(f"Gender: {gender}") 
        print(f"Product ID: {product_id}")
        print(f"Description: {description}")
        print(f"Product Name: {product_name}")
        print(f"Price: {price}")

    except (NoSuchElementException, TimeoutException) as e:
        print(f"Error encountered while processing product: {e}")

# Close the browser
driver.quit()


# In[78]:


# Set up WebDriver with a proxy
driver = setup_driver_with_proxy(proxies)

# Convert the set to a list
unique_product_links_list = list(unique_product_links)

# Initialize an empty list to store product details
product_details_list = []

# Iterate through all links in the list
for product_url in unique_product_links_list:
    try:
        # Navigate to the product page
        driver.get(product_url)
        
        try:
            # Handle captcha (assuming you have a class named `AmazonCaptcha`)
            captcha_link = driver.find_element(By.XPATH , "/html/body/div/div[1]/div[3]/div/div/form/div[1]/div/div/div[1]/img").get_attribute('src')
            captcha = AmazonCaptcha.fromlink(captcha_link)
            captcha_value = AmazonCaptcha.solve(captcha)
            input_field = driver.find_element(By.ID , "captchacharacters")
            input_field.send_keys(captcha_value)

            button = driver.find_element(By.CLASS_NAME, "a-button-text")
            button.click()

        except:
            # Wait for page to load (adjust timeout as needed)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "productTitle")))

            # Get page source
            page_source = driver.page_source

            # Parse HTML content
            soup = BeautifulSoup(page_source, 'html.parser')

            # Extract product details
            product_name = soup.find("span", id="productTitle").text.strip()
            description = soup.find("div", id="productDescription").text.strip()
            price_span = soup.find('span', class_='aok-offscreen')
            price = price_span.text.strip() if price_span else "Price information not found."

            asin_element = driver.find_element(By.CSS_SELECTOR, '#detailBullets_feature_div > ul > li:nth-child(5) > span > span:nth-child(2)')
            product_id = asin_element.text.strip()

            brand_element = driver.find_element(By.CSS_SELECTOR, '#detailBullets_feature_div > ul > li:nth-child(4) > span > span:nth-child(2)')
            brand_name = brand_element.text.strip()

            b_element = driver.find_element(By.CSS_SELECTOR, '#wayfinding-breadcrumbs_feature_div > ul > li:nth-child(5) > span > a')
            category = b_element.text.strip()

            c_element = driver.find_element(By.CSS_SELECTOR, '#wayfinding-breadcrumbs_feature_div > ul > li:nth-child(7) > span > a')
            sub_category = c_element.text.strip()

            g_element = driver.find_element(By.CSS_SELECTOR, '#wayfinding-breadcrumbs_feature_div > ul > li:nth-child(3) > span > a')
            gender = g_element.text.strip()

            # Extract product reviews (replace with desired review scraping logic)
            # Replace this placeholder with your implementation to scrape reviews and rankings
            product_reviews = []

            # Store product details in a dictionary
            product_details = {
                "productUrl": product_url,
                "productId": product_id,
                "gender": gender,
                "category": category,
                "description": description,
                "subCategory": sub_category,
                "productName": product_name,
                "brandName": brand_name,
                "price": price
            }

            # Append the product details to the list
            product_details_list.append(product_details)

    except (NoSuchElementException, TimeoutException) as e:
        print(f"Error encountered while processing product {product_url}: {e}")

# Close the browser
driver.quit()


# In[79]:


# Save product details to a JSON file
output_filename = 'i211715_amazon.json'
with open(output_filename, 'w') as json_file:
    json.dump(product_details_list, json_file, indent=2)

print(f"Product details saved to {output_filename}")


# In[ ]:




