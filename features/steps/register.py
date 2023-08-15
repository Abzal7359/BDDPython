from datetime import datetime

from behave import *

from features.pages.HomePage import HomePage
from features.pages.RegisterPage import RegisterPage
from utilities import automailGenerator

pas = "901@Abn"


# def automail():  # this is for  generating random mails
#     timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
#     return "abzal" + timestamp + "@gmail.com"


store = "O170700@rguktong.ac.in"


@given(u'I navigates to register page')
def step_impl(context):
    HP = HomePage(context.driver)
    HP.clickOnMyAccount()
    context.RP=HP.clickOnRegister()  #here RP pom object is getting we returning from home page



@when(u'I enters below in mandatory fields')
def step_impl(context):
    for row in context.table:
        automail=automailGenerator.automail()
        context.RP.enter_details(row["firstname"],row["lastname"], automail,row["phone"],row["password"])


@when(u'I click continue button')
def step_impl(context):
    context.RP.clickContinue()



@then(u'Account should get created')
def step_impl(context):
    assert context.RP.isAccountCreated()

@when(u'I enters all fields')
def step_impl(context):
    for row in context.table:
        automail = automailGenerator.automail()
        context.RP.enter_details(row["firstname"], row["lastname"], automail, row["phone"], row["password"])

    context.RP.click_newsletter_yes()


@when(u'I enters all fields expect mail field')
def step_impl(context):
    context.RP.enter_details_noMail("harish", "chandra", "9067123231", pas)
    context.RP.click_newsletter_yes()


@when(u'I enter existing account mail into mail field')
def step_impl(context):
    context.RP.enterExistingMail(store)


@then(u'proper warning message should display')
def step_impl(context):
    assert context.RP.proper_warn()


@when(u'I dont anything into fields')
def step_impl(context):
    pass


@then(u'proper warning message should display for mandatory fields')
def step_impl(context):
    assert context.RP.mandatory_warn()
