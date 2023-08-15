import time
from datetime import datetime

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from features.pages.HomePage import HomePage
from features.pages.LoginPage import LoginPage
from utilities import automailGenerator


# def automail(): #this is for  generating random mails
#     timestamp=datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
#     return "abzal"+timestamp+"@gmail.com"

@given(u'user navigates to login page')
def step_impl(context):
    context.HP=HomePage(context.driver)
    context.HP.clickOnMyAccount()
    context.LP=context.HP.clickOnLogin() #this line has LP object


@when(u'user enters valid email address email "{email}" and password "{password}"')
def step_impl(context,email,password):

    # LP=LoginPage(context.driver)
    context.LP.enter_email_and_password(email,password)


@then(u'user should login succesfully')
def step_impl(context):
    # LP = LoginPage(context.driver)
    assert context.LP.isLoginSucces()

@when(u'user enters INvalid email address "{email}" and INvalid password "{password}"')
def step_impl(context,email,password):
    # LP = LoginPage(context.driver)
    context.LP.enter_email_and_password(email, password)

@when(u'clicks login button')
def step_impl(context):
    # LP = LoginPage(context.driver)
    context.LP.clickLoginButton()

@then(u'user should get proper warning message')
def step_impl(context):
    # LP = LoginPage(context.driver)
    assert context.LP.warning_message()

@when(u'user enters valid email address and Invalid password')
def step_impl(context):
    # LP = LoginPage(context.driver)
    context.LP.enter_email_and_password("O170700@rguktong.ac.in","7359@Abza")

@when(u'user enters INvalid email address and valid password')
def step_impl(context):
    # LP = LoginPage(context.driver)
    automail = automailGenerator.automail()
    context.LP.enter_email_and_password(automail,"7359@Abzal")

@when(u'user doesnt enter any credintials')
def step_impl(context):
    pass
