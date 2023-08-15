from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):
        self.driver=driver
    email_XPATH="//input[@id='input-email']"
    password_XPATH="//input[@id='input-password']"
    login_button_XPATH="//input[@value='Login']"
    isLoginSuccess_XPATH="//a[normalize-space()='Edit your account information']"
    warning_message_XPATH="//div[@class='alert alert-danger alert-dismissible']"
    def enter_email_and_password(self,email,password):
        self.driver.find_element(By.XPATH,self.email_XPATH).clear()
        self.driver.find_element(By.XPATH, self.email_XPATH).send_keys(email)

        self.driver.find_element(By.XPATH, self.password_XPATH).clear()
        self.driver.find_element(By.XPATH, self.password_XPATH).send_keys(password)
    def clickLoginButton(self):
        self.driver.find_element(By.XPATH, self.login_button_XPATH).click()
    def isLoginSucces(self):
        b=self.driver.find_element(By.XPATH,self.isLoginSuccess_XPATH).is_displayed()
        return b
    def warning_message(self):
        c=self.driver.find_element(By.XPATH,self.warning_message_XPATH).is_displayed()
        return c