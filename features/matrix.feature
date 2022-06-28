Feature: Requirements Matrix

    Scenario: Create Matrix
        Given I am on the project overview page
        Given I select a project with an Requirement Analysis Stage
        Then I am on the specific project page
        When I click create requirements matrix 
        Then a popup confirms a matrix was created 
    
    Scenario: Add Requirement
        Given I am on the the specific project page 
        Given There is a created matrix
        When I click add requirement 
        Then a form appears 
        When I type in a user story or rule into the user-story or rule input
        When I select a priority level
        When I type a note into the note input 
        When I click add
        Then the requirement is added to the matrix table

    Scenario: Finish Initial Matrix
        Given I have added at least one requirement
        Then I should see an option to continue
        When I click continue 
        Then STLC stage should be listed as Test Planning
    
    Scenario: Add Test Case To Requirement
        Given 