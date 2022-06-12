from enum import Enum
from typing import Literal
from pydantic import BaseModel

class LoginCredentials(BaseModel):
    username: str 
    password: str 

class EmployeeRecord(BaseModel):
    username: str 
    password: str 
    fname: str 
    lname: str
    role: Literal["Tester"] | Literal["Manager"]

class Employee(BaseModel):
    username: str
    fname: str 
    lname: str
    role: Literal["Tester"] | Literal["Manager"]


class DefectUpdate(BaseModel):
    status: Literal["Pending"] | Literal["Accepted"] | Literal["Rejected"] | Literal["Fixed"] | Literal["Declined"] | Literal["Shelved"]

class DefectForm(BaseModel):
    assignedTo: str
    dateReported: int
    desc: str 
    stepsToReproduce: str 
    severity: Literal["Low"] | Literal["Medium"] | Literal["High"]
    priority: Literal["Low"] | Literal["Medium"] | Literal["High"] 


class Defect(BaseModel):
    defectId: int 
    assignedTo: str
    dateReported: int

    status: Literal["Pending"] | Literal["Accepted"] | Literal["Rejected"] | Literal["Fixed"] | Literal["Declined"] | Literal["Shelved"]
    desc: str 
    stepsToReproduce: str 
    severity: Literal["Low"] | Literal["Medium"] | Literal["High"]
    priority: Literal["Low"] | Literal["Medium"] | Literal["High"]  


class TestEnum(str, Enum):
    performance = "Performance"
    acceptance = "Acceptance"
    functional = "Functional"
    smoke = "Smoke"
    regression = "Regression"
    retesting = "Retesting"


class ProjectForm(BaseModel):
    title: str 
    about: str


class Project(BaseModel):
    projectId: int
    title: str 
    about: str

class TestCaseForm(BaseModel):
    summaryId: int
    featureTested: str 
    desc: str 
    isAutomated: bool
    result: Literal["Pass"] | Literal["Fail"] | Literal["Flaky"]
    posOrNeg: Literal["Positive"] | Literal["Negative"]
    boxType: Literal["Whitebox"] | Literal["Blackbox"] | Literal["Greybox"]

    
class TestCase(BaseModel):
    caseId: int 
    summaryId: int
    testedBy: str

    featureTested: str 
    desc: str 
    isAutomated: bool
    result: Literal["Pass"] | Literal["Fail"] | Literal["Flaky"]
    posOrNeg: Literal["Positive"] | Literal["Negative"]
    boxType: Literal["Whitebox"] | Literal["Blackbox"] | Literal["Greybox"]

class TestSummaryForm(BaseModel):
    projectId: int

    startDate: int
    endDate: int

    featuresInScope: list[str]
    testEnvironmentDesc: str
    objectives: list[TestEnum]
    reasonForTesting: str
    overallResulstDesc: str    

class TestSummary(BaseModel):
    summaryId: int
    projectId: int

    startDate: int
    endDate: int

    featuresInScope: list[str]
    testEnvironmentDesc: str
    objectives: list[TestEnum]
    reasonForTesting: str

    testCases: list[TestCase] 
    overallResulstDesc: str
    isFinalized: bool
    