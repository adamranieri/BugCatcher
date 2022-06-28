Feature: Project Management

    Scenario: Create a new Project 
        Given I am on the Manager home page
        When I click create new project 
        Then a project form appears
        When I type in project title
        When I type in project description
        When I press submit
        Then a pop up confirms my project was added successfully
        Then STLC stage should be listed as Requirement Analysis
    
    Scenario: Select a project
        Given I am on the Manager home page 
        Then I should be able to see all projects
        When I click on the project 
        Then I should be on the the specific project page for that project

    Scenario: Add Test documents
        Given I am on the specific project page for a project 
        Given the STLC stage is Test Planning
        Then the screen should say to upload a test plan and test strategy
        When I upload a test plan document 
        When I upload a test strategy 
        When I click submit 
        Then an alert should say it was successfully added 
        Then The STLC stage should be listed as Test Case Development
    
        
        