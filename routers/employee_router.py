from fastapi import APIRouter, HTTPException, Header

from models.employee_models import Employee, EmployeeRecord, LoginCredentials, Role

router = APIRouter()

employees_store = {}

for i in range(1,100):
    employees_store[f"{i}"] = [
        EmployeeRecord(username="adamGator", fname="Adam", lname="Ranieri", password="pass123", role=Role.MANAGER),
        EmployeeRecord(username="ryan99", fname="Ryan", lname="Schlientz", password="coolbeans", role=Role.TESTER),
        EmployeeRecord(username="Sierra117", fname="Sierra", lname="Nichols", password="superpa$$", role=Role.TESTER)
    ]

employees: list[EmployeeRecord] = [
    EmployeeRecord(username="g8tor", fname="Patty", lname="Pastiche", password="chomp!", role=Role.MANAGER),
    EmployeeRecord(username="ryeGuy", fname="Fakey", lname="McFakeFace", password="coolbeans", role=Role.TESTER),
    EmployeeRecord(username="cavalier89", fname="Dracula", lname="Fangs", password="alucard", role=Role.TESTER),
    ]


@router.patch("/login", response_model=Employee)
def login(credentials: LoginCredentials, dev: str = Header(default="0")) -> Employee:
    print(dev)

    employee: EmployeeRecord | None = next((e for e in employees if e.username == credentials.username), None) 
    
    if employee is None:
        raise HTTPException(404,"No user with that username")
    elif employee.password != credentials.password:
        raise HTTPException(403,f"Incorrect password for {credentials.username}")
    else:
        return Employee(**employee.dict())

@router.put('/employees', response_model=Employee, status_code=201)
def create_employee(emp: EmployeeRecord, dev: str = Header(default="0")) -> Employee:

    for e in employees:
        if e.username == emp.username:
            raise HTTPException(400,f'Employee with username {emp.username} already exists')
    else:
        employees.append(emp)
        return Employee(**emp.dict())

@router.get("/employees")
def get_all_employees(dev: str = Header(default="0")):
    return [Employee(**e.dict()) for e in employees]