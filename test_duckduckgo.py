from selenium import webdriver
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

    # Pause so the browser stays open
    input("Press Enter to close the browser...")
    driver.quit()

if __name__ == "__main__":
    test_duckduckgo_search()

 
