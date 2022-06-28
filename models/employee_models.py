from enum import Enum
from pydantic import BaseModel

class Role(str, Enum):
    TESTER = "TESTER"
    MANAGER = "MANAGER"


class LoginCredentials(BaseModel):
    username: str 
    password: str 

class EmployeeRecord(BaseModel):
    username: str 
    password: str 
    fname: str 
    lname: str
    role: Role

class Employee(BaseModel):
    username: str
    fname: str 
    lname: str
    role: Role