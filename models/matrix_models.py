from pydantic import BaseModel
from enums import Level, TestResult
from models.test_documents import TestPlan, TestStrategy



class Requirement(BaseModel):
    userStoryOrRule: str 
    testCases: list[int]
    defectIds: list[int]
    priority: Level
    note: str


class TestCase(BaseModel):
    caseId: int 
    desc: str
    steps: str 
    result: TestResult
    performedBy: str | None
    isAutomated: bool
    

class Matrix(BaseModel):
    matrixId: int
    title: str 
    requirements: list[Requirement]

class MatrixForm(BaseModel):
    title: str
