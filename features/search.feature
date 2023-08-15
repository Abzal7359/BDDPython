Feature: searching for products
#  Background:
#    Given user opens the application
  @search
  Scenario: search for valid product
    Given user opens the application
    When enter valid product into search field "hp"
    And click on search button
    Then valid product should get displayed in search results
  @search @v
  Scenario: search for INvalid product
    Given user opens the application
    When enter INvalid product "honda" into search field
    And click on search button
    Then proper text display no product matching should display
  @search
  Scenario: search without providing any product
    Given user opens the application
    When user doesnt enter any product name into search field
    And click on search button
    Then proper text display no product matching should display