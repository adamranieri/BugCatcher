from pydantic import BaseModel
from enums import TestLevel, TestType


class Objective(BaseModel):
    feature: str 
    level: TestLevel
    testType: TestType

class TestStrategy(BaseModel):  
    testApproach: str
    testEnvironment: str 
    testTools: str 
    bugReporting: str
    risks: str

class Deadline(BaseModel):
    desc: str
    date: int 

class TestPlan(BaseModel):
    planId: int 
    deadlines: list[Deadline]
    featuresInScope: list[Objective]
    featuresOutScope: list[Objective]
