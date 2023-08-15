import allure
from allure_commons.types import AttachmentType
from selenium import webdriver

def before_scenario(context,driver):
    url = "https://tutorialsninja.com/demo/"
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    context.driver = webdriver.Chrome(options=options)
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.get(url)
def after_scenario(context,driver):
    context.driver.quit()

def after_step(context,step):
    if step.status=="failed":
        allure.attach(context.driver.get_screenshot_as_png()
                      ,name="failed_screenshot"
                      ,attachment_type=AttachmentType.PNG)

