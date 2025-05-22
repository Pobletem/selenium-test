from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# import logging


def test_duckduckgo_search():
    driver = webdriver.Chrome()
    driver.get("https://duckduckgo.com")

    try:
        # QA Concept: Assert correct page title
        assert "DuckDuckGo" in driver.title, "FAIL: Title mismatch"

        print("PASS: Title matches what was searched")

        # Locate the search box element and search a term
        # q is the element name of the search box, it stands for 'query'
        searchBox = driver.find_element(By.NAME, "q")
        searchBox.send_keys("Selenium WebDriver" + Keys.RETURN)

        time.sleep(3)

        # Here we are grabbing all the elements in the css class result
        # in the case of duckduckgo the tag for results is article
        results = driver.find_elements(By.CSS_SELECTOR, "article[data-nrn]")

        # QA concept, ensuring there are results showing as expected
        assert len(results) > 0, "FAIL: No results found"

        # Printing all the results found
        print(f"PASS: Found {len(results)} results")
    finally:
        driver.quit()


def test_valid_login():
    driver = webdriver.Chrome()
    # Go to the test website for login testing
    driver.get("https://the-internet.herokuapp.com/login")

    try:
        # finds the username and password fields
        passwordField = driver.find_element(By.ID, "password")
        usernameField = driver.find_element(By.ID, "username")
        # Inputs valid credentials
        usernameField.send_keys("tomsmith")
        passwordField.send_keys("SuperSecretPassword!")

        # finds the submit button for login and sends the click command
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # QA Assertion: Check that login was successful
        # finds the class of the flash ui element
        flashClass = driver.find_element(By.ID, "flash")
        # Saving the text that shows up in the alert message
        successMessage = flashClass.text

        # Test class of the flash ui ensuring its correct
        assert "success" in flashClass.get_attribute("class"), (
            "FAIL: Unexpected class"
        )

        print("PASS: Valid login flash class used")

        # Test text inside flash ui ensuring its correct
        assert "You logged into a secure area!" in successMessage, (
            "FAIL: Login failed"
        )

        print("PASS: Valid login successful")

        time.sleep(3)
    finally:
        driver.quit()


def test_invalid_login():
    driver = webdriver.Chrome()
    # Go to the test website for login testing
    driver.get("https://the-internet.herokuapp.com/login")

    try:
        # finds the username and password fields
        passwordField = driver.find_element(By.ID, "password")
        usernameField = driver.find_element(By.ID, "username")
        # Inputs invalid credentials
        usernameField.send_keys("wronguser")
        passwordField.send_keys("superwrongpassword")

        # finds the submit button for login and sends the click command
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # QA Assertion: Check that login was a failure
        # finds the class of the flash ui element
        flashClass = driver.find_element(By.ID, "flash")
        # Saving the text that shows up in the alert message
        errorMessage = flashClass.text

        # Test class of the flash ui ensuring it matches the error class
        assert "error" in flashClass.get_attribute("class"), (
            "FAIL: Unexpected class"
        )
        print("PASS: Proper failure login flash class used")

        # Test text of the flash ui ensuring its correct
        assert "Your username is invalid!" in errorMessage, (
            "FAIL: Invalid login not handled properly"
        )

        print("PASS: Invalid login properly handled")

        time.sleep(3)
    finally:
        driver.quit()


if __name__ == "__main__":
    test_duckduckgo_search()
    test_valid_login()
    test_invalid_login()
