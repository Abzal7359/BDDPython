from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from features.pages.HomePage import HomePage
from features.pages.SearchPage import SearchPage


@given(u'user opens the application')
def step_impl(context):
    expected_title="Your Store"
    assert context.driver.title == expected_title

@when(u'enter valid product into search field "{product}"')
def step_impl(context,product):
    context.HP=HomePage(context.driver)
    context.HP.enterIntoSearch(product)



@when(u'click on search button')
def step_impl(context):
    context.HP = HomePage(context.driver)
    context.SP=context.HP.clickOnSearch()  #in these line we getting search page object due to we return searchPage object after click function


@then(u'valid product should get displayed in search results')
def step_impl(context):
    # SP=SearchPage(context.driver)
    assert context.SP.validProductIsDisplayed()



@when(u'enter INvalid product "{prod}" into search field')
def step_impl(context,prod):
    context.HP = HomePage(context.driver)
    context.HP.enterIntoSearch(prod)


@then(u'proper text display no product matching should display')
def step_impl(context):
    # SP = SearchPage(context.driver)
    assert not context.SP.InvalidProductWarning()


@when(u'user doesnt enter any product name into search field')
def step_impl(context):
    context.HP = HomePage(context.driver)
    context.HP.enterIntoSearch("")