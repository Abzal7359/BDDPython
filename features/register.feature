Feature: user Registration

  @reg
  Scenario: register with mandatory fields
    Given I navigates to register page
    When I enters below in mandatory fields
    |firstname|lastname|phone     |password |
    |harish   |chandra |8674512021|901@Abn  |
    And I click continue button
    Then Account should get created

  @reg
  Scenario: register with mandatory and  all fields
    Given I navigates to register page
    When I enters all fields
    |firstname|lastname|phone     |password |
    |harish   |chandra |8674512021|901@Abn  |
    And I click continue button
    Then Account should get created

  @reg
  Scenario: register with duplicate mail address
    Given I navigates to register page
    When I enters all fields expect mail field
    And I enter existing account mail into mail field
    And I click continue button
    Then proper warning message should display
  @reg
  Scenario: register without any fields
    Given I navigates to register page
    When I dont anything into fields
    And I click continue button
    Then proper warning message should display for mandatory fields