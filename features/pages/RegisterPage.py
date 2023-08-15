from selenium.webdriver.common.by import By


class RegisterPage:
    def __init__(self,driver):
        self.driver=driver

    firstname_XPATH="//input[@id='input-firstname']"
    lastname_XPATH="//input[@id='input-lastname']"
    email_XPATH="//input[@id='input-email']"
    telephone_XPATH="//input[@id='input-telephone']"
    password_XPATH="//input[@id='input-password']"
    confirmPassword_XPATH="//input[@id='input-confirm']"
    agree_XPATH="//input[@name='agree']"
    continue_XPATH="//input[@value='Continue']"
    AccountCreated_XPATH="//h1[normalize-space()='Your Account Has Been Created!']"
    mandatory_warn_XPATH="(//div[contains(text(),'First Name must be between 1 and 32 characters!')])[1]"
    proper_warn_XPATH="(//div[@class='alert alert-danger alert-dismissible'])[1]"
    newsLetter_XPATH="(//input[@name='newsletter'])[1]"
    def enter_details(self,fn,ln,email,phone,pw):
        self.driver.find_element(By.XPATH,self.firstname_XPATH).send_keys(fn)
        self.driver.find_element(By.XPATH, self.lastname_XPATH).send_keys(ln)
        self.driver.find_element(By.XPATH, self.email_XPATH).send_keys(email)
        self.driver.find_element(By.XPATH, self.telephone_XPATH).send_keys(phone)
        self.driver.find_element(By.XPATH, self.password_XPATH).send_keys(pw)
        self.driver.find_element(By.XPATH, self.confirmPassword_XPATH).send_keys(pw)
        self.driver.find_element(By.XPATH, self.agree_XPATH).click()

    def enter_details_noMail(self,fn,ln,phone,pw):
        self.driver.find_element(By.XPATH,self.firstname_XPATH).send_keys(fn)
        self.driver.find_element(By.XPATH, self.lastname_XPATH).send_keys(ln)

        self.driver.find_element(By.XPATH, self.telephone_XPATH).send_keys(phone)
        self.driver.find_element(By.XPATH, self.password_XPATH).send_keys(pw)
        self.driver.find_element(By.XPATH, self.confirmPassword_XPATH).send_keys(pw)
        self.driver.find_element(By.XPATH, self.agree_XPATH).click()

    def clickContinue(self):
        self.driver.find_element(By.XPATH,self.continue_XPATH).click()
    def isAccountCreated(self):
        return self.driver.find_element(By.XPATH, self.AccountCreated_XPATH).is_displayed()
    def enterExistingMail(self,email):
        self.driver.find_element(By.XPATH, self.email_XPATH).send_keys(email)
    def mandatory_warn(self):
        return self.driver.find_element(By.XPATH,self.mandatory_warn_XPATH).is_displayed()
    def proper_warn(self):
        return self.driver.find_element(By.XPATH, self.proper_warn_XPATH).is_displayed()
    def click_newsletter_yes(self):
        self.driver.find_element(By.XPATH, self.newsLetter_XPATH).click()