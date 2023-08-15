from selenium.webdriver.common.by import By


class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    validProduct_XPATH = "//a[normalize-space()='HP LP3065']"
    NoProduct_matching_XPATH = "(//p[contains(text(),'There is no product that matches the search criter')])[1]"

    def validProductIsDisplayed(self):
        return self.driver.find_element(By.XPATH, self.validProduct_XPATH).is_displayed()

    def InvalidProductWarning(self):
        return self.driver.find_element(By.XPATH, self.NoProduct_matching_XPATH).is_displayed()
