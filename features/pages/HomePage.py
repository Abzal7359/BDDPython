from selenium.webdriver.common.by import By

from features.pages.LoginPage import LoginPage
from features.pages.RegisterPage import RegisterPage
from features.pages.SearchPage import SearchPage


class HomePage:
    def __init__(self,driver):
        self.driver=driver
    myAccount_XPATH="//ul[@class='list-inline']//li[@class='dropdown']"
    login_XPATH="//a[normalize-space()='Login']"
    register_XPATH="(//a[normalize-space()='Register'])[1]"
    searchInput_XPATH="//input[@placeholder='Search']"
    searchButton_XPATH="//button[@class='btn btn-default btn-lg']"


    def clickOnMyAccount(self):
        self.driver.find_element(By.XPATH,self.myAccount_XPATH).click()
    def clickOnLogin(self):
        self.driver.find_element(By.XPATH, self.login_XPATH).click()
        return LoginPage(self.driver)

    def clickOnRegister(self):
        self.driver.find_element(By.XPATH, self.register_XPATH).click()
        return RegisterPage(self.driver)

    def enterIntoSearch(self,item):
        self.driver.find_element(By.XPATH, self.searchInput_XPATH).clear()
        self.driver.find_element(By.XPATH, self.searchInput_XPATH).send_keys(item)

    def clickOnSearch(self):
        self.driver.find_element(By.XPATH, self.searchButton_XPATH).click()
        return SearchPage(self.driver)