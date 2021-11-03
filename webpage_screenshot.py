from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Define URL
url = 'https://www.jcchouinard.com/python-for-seo/'
path = 'output/scrape.png'

# Start driver
driver = webdriver.Chrome(ChromeDriverManager().install())

# Go to URL
driver.get(url)

# Save content as image file
content = driver.find_element_by_tag_name('body')
content.screenshot(path)

# close webdriver
driver.quit()