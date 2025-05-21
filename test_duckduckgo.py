from selenium import webdriver


def test_duckduckgo_search():
    driver = webdriver.Chrome()
    driver.get("https://duckduckgo.com")

    # QA Concept: Assert correct page title
    assert "DuckDuckGo" in driver.title, "FAIL: Title mismatch"

    # Pause so the browser stays open
    input("Press Enter to close the browser...")
    driver.quit()

if __name__ == "__main__":
    test_duckduckgo_search()

 
