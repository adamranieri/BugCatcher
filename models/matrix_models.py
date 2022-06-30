from pydantic import BaseModel
from .enums import Level


class Requirement(BaseModel):
    userStoryOrRule: str 
    testCases: list[int]
    defectIds: list[int]
    priority: Level
    note: str

class Matrix(BaseModel):
    matrixId: int
    title: str 
    requirements: list[Requirement]

class MatrixForm(BaseModel):
    title: str
