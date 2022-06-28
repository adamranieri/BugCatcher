Feature: Test Case Development

    Scenario: Add Test Case 
        Given I am on the Test Case Creation page 
        When I type description into the description input
        When I type steps into the steps input
        When I click add Test Case 
        Then an alert should confirm a test case was addded
        Then the form should be empty