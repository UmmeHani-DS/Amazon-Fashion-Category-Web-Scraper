# Amazon Fashion Category Web Scraper

### Introduction
This project involves creating a web scraper to gather detailed information about products in the 'Fashion' category on Amazon. Using web scraping techniques, the goal is to collect data on at least 1000 products from each subcategory, such as shoes, clothes, watches, etc. The data will be organized in JSON format for easy analysis and understanding of trends and popular items in the Amazon Fashion category.

### Objectives
- Scrape detailed product information from the Amazon Fashion category.
- Store the scraped data in JSON format.
- Analyze the collected data to understand buying trends and popular products.

### Data to be Collected
For each product, the following information will be gathered:
1. **Product URL**: The web address for the product.
2. **Product ID**: Unique identifier for the product.
3. **Gender**: Target gender for the product (if applicable).
4. **Category**: Broad category such as "Accessories."
5. **Description**: Detailed write-up about the product.
6. **Product Name**: Official name of the product.
7. **Sub Category**: Specific group within the main category.
8. **Brand Name**: Manufacturer or seller of the product.
9. **Colours**: Available color options for the product.
10. **Images**: URLs of product images.
11. **Price**: Cost of the product, including sale prices.
12. **Product Reviews and Ratings**: Customer reviews and star ratings.

### Tasks
1. **Scrape Product Information**:
    - Extract URLs of at least 10 different subcategories within the Fashion category.
    - Gather information on at least 1000 products from each subcategory.
2. **Store Image URLs**:
    - Extract and save URLs of product images.
    - Organize image URLs based on relevance, such as primary images or different color options.
3. **Collect Product Reviews**:
    - Extract review text, star ratings, and reviewer information.
    - Handle pagination to scrape reviews from multiple pages.
4. **Error Handling**:
    - Handle cases where product availability, description, or certain entities are not present by storing them as `None` or `null`.
    - Implement error handling for HTTP errors, timeouts, and other network issues.
5. **Pagination Handling**:
    - Identify and handle pagination elements on category pages to scrape multiple pages of products.
6. **Efficiency Optimization**:
    - Configure scripts to respect Amazon's rate limits and scraping policies.
    - Use request headers to mimic legitimate user behavior and avoid detection.
    - Implement proxy rotation to distribute requests across multiple IP addresses.
7. **Data Validation**:
    - Perform data validation checks to ensure accuracy and completeness.
    - Compare scraped data with a sample of manually verified data to identify discrepancies.
8. **Documentation**:
    - Document the scraping process and provide instructions for running the scripts.

### Technologies Used
- **Selenium**: For navigating and interacting with dynamic web pages.
- **Beautiful Soup**: For parsing HTML and extracting data.
- **JSON**: For storing the collected data.
- **fuzzywuzzy**: For sub-category classification based on product names.
  
---

This project provides a comprehensive approach to scraping and analyzing product data from the Amazon Fashion category, leveraging various web scraping techniques and tools.
