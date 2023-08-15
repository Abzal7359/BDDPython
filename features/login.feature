Feature: User Login
  @l @z
  Scenario:Login with valid cred
    Given user navigates to login page
    When user enters valid email address email "O170700@rguktong.ac.in" and password "7359@Abzal"
    And clicks login button
    Then user should login succesfully


  @login @y
  Scenario Outline:Login with Invalid cred
    Given user navigates to login page
    When user enters INvalid email address "<email>" and INvalid password "<password>"
    And clicks login button
    Then user should get proper warning message
    Examples:
    |email                  |       password    |
    |O170700@rgukton.ac.in  |        7359@12    |
    |O17070@rgukton.ac.in   |       123@Abza    |
    |O170700@rguktong.ac.in |     12457!dilli   |
    |asdfgh@gmai.com        | 73597359@Abzal    |

  @l
  Scenario:Login with valid email address and Invalid password
    Given user navigates to login page
    When user enters valid email address and Invalid password
    And clicks login button
    Then user should get proper warning message
  @l
  Scenario:Login with Invalid email address and valid password
    Given user navigates to login page
    When user enters INvalid email address and valid password
    And clicks login button
    Then user should get proper warning message
  @l
  Scenario:Login without any  credintials
    Given user navigates to login page
    When user doesnt enter any credintials
    And clicks login button
    Then user should get proper warning message
