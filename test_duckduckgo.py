from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import logging

def test_duckduckgo_search():
    driver = webdriver.Chrome()
    driver.get("https://duckduckgo.com")

    # Set up logging
    # Sets logging level to info and makes the format display the level name and then a message
    logging.basicConfig(level=logging.INFO, format='\n%(levelname)s: %(message)s\n')

    # Prints the title of the website for logging reasons
    logging.info("Title is: %s", driver.title)

    # QA Concept: Assert correct page title
    assert "DuckDuckGo" in driver.title, "FAIL: Title mismatch"

    # Locate the search box element and search a term
    # q is the element name of the search box, it stands for 'query'
    searchBox = driver.find_element(By.NAME, "q") 
    searchBox.send_keys("Selenium WebDriver" + Keys.RETURN)

    # Here we are grabbing all the elements in the css class result that are inside the css class results
    results = driver.find_elements(By.CSS_SELECTOR, ".results .result")

    # QA concept, ensuring there are results showing as expected
    assert len(results) > 0, "FAIL: No results found"

    # Printing all the results found
    print(f"PASS: Found {len(results)} results")

    # Pause so the browser stays open
    input("Press Enter to close the browser...")
    driver.quit()

if __name__ == "__main__":
    test_duckduckgo_search()

 
