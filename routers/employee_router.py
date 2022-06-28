from fastapi import APIRouter, HTTPException

from models.employee_models import Employee, EmployeeRecord, LoginCredentials, Role

router = APIRouter()

employees: list[EmployeeRecord] = [
    EmployeeRecord(username="adamGator", fname="Adam", lname="Ranieri", password="pass123", role=Role.MANAGER),
    EmployeeRecord(username="ryan99", fname="Ryan", lname="Schlientz", password="coolbeans", role=Role.TESTER),
    EmployeeRecord(username="Sierra117", fname="Sierra", lname="Nichols", password="superpa$$", role=Role.TESTER)
    ]


@router.patch("/login", response_model=Employee)
def login(credentials: LoginCredentials) -> Employee:

    employee: EmployeeRecord | None = next((e for e in employees if e.username == credentials.username), None) 
    
    if employee is None:
        raise HTTPException(404,"No user with that username")
    elif employee.password != credentials.password:
        raise HTTPException(403,f"Incorrect password for {credentials.username}")
    else:
        return Employee(**employee.dict())

@router.put('/employees', response_model=Employee, status_code=201)
def create_employee(emp: EmployeeRecord) -> Employee:

    for e in employees:
        if e.username == emp.username:
            raise HTTPException(400,f'Employee with username {emp.username} already exists')
    else:
        employees.append(emp)
        return Employee(**emp.dict())

@router.get("/employees")
def get_all_employees():
    return [Employee(**e.dict()) for e in employees]