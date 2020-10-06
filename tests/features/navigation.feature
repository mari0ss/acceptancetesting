Feature: Test navigation between pages
  We can have a longer description

  Scenario: Homepage can go to blog
    Given I am on the homepage
    When I click on the "Go to blog" link
    Then I am on the blog page


  Scenario: blog can go to homepage
    Given I am on the blog page
    When I click on the "Go to home" link
    Then I am on the homepage
