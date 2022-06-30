from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles

from fastapi.middleware.cors import CORSMiddleware
from random import randint

from models.defect_models import Defect

from models.employee_models import EmployeeRecord, Role
from models.enums import DefectStatus, Level

from routers.employee_router import router as employee_router
from routers.defect_router import router as defect_router
from routers.case_router import router as case_router



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )

app.include_router(employee_router)
app.include_router(defect_router)    
app.include_router(case_router)


@app.delete('/debug/nuke', status_code=204)
def destroy_all():
    employees.clear()
    defects.clear()


@app.delete("/debug/reset")
def sample_data():
    global employees 
    employees = [EmployeeRecord(username="adamGator", fname="Adam", lname="Ranieri", password="pass123", role=Role.MANAGER), EmployeeRecord(username="ryan99", fname="Ryan", lname="Schlientz", password="coolbeans", role=Role.TESTER) ]

    global defects
    defects = [Defect(defectId=101, assignedTo="Billy", dateReported=10000, status=DefectStatus.PENDING, severity=Level.LOW, priority=Level.HIGH, desc="Sample", stepsToReproduce="1. does not actually exist")]

