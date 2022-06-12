from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles

from models import Defect, DefectForm, DefectUpdate, Employee, EmployeeRecord, LoginCredentials, Project, ProjectForm, TestCase, TestCaseForm, TestSummary, TestSummaryForm
from fastapi.middleware.cors import CORSMiddleware
from random import randint


app = FastAPI()

app.mount("/web", StaticFiles(directory="web"), name="web")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )

employees: list[EmployeeRecord] = [
    EmployeeRecord(username="adamGator", fname="Adam", lname="Ranieri", password="pass123", role="Manager"),
    EmployeeRecord(username="ryan99", fname="Ryan", lname="Schlientz", password="coolbeans", role="Tester") 
    ]

defects: list[Defect] = [
    Defect(defectId=101, assignedTo="Billy", dateReported=10000, status="Pending", severity="Low", priority="High", desc="Sample", stepsToReproduce="1. does not actually exist")
    ]

projects: list[Project] = []

summaries: list[TestSummary] = []

cases: list[TestCase] = []

#Login

@app.patch("/login", response_model=Employee)
def login(credentials: LoginCredentials) -> Employee:

    employee: EmployeeRecord | None = next((e for e in employees if e.username == credentials.username), None) 
    
    if employee is None:
        raise HTTPException(404,"No user with that username")
    elif employee.password != credentials.password:
        raise HTTPException(403,f"Incorrect password for {credentials.username}")
    else:
        return Employee(**employee.dict())

@app.put('/employees', response_model=Employee, status_code=201)
def create_employee(emp: EmployeeRecord) -> Employee:

    for e in employees:
        if e.username == emp.username:
            raise HTTPException(400,f'Employee with username {emp.username} already exists')
    else:
        employees.append(emp)
        return Employee(**emp.dict())

@app.get("/employees")
def get_all_employees():
    return [Employee(**e.dict()) for e in employees]

## Defect Reporter

@app.post("/defects", response_model=Defect, status_code=201)
def create_defect(defect_form: DefectForm) -> Defect:
    defect = Defect(defectId=randint(10000,99999), **defect_form.dict(), status="Pending")

    for emp in employees:
        if emp.username == defect.assignedTo:
            break
    else:
        raise HTTPException(404, f'Could not find an employee with username {defect.assignedTo}')

    defects.append(defect)
    return defect



@app.patch("/defects/{defectId}", status_code=204)
def update_defect(defectId: int, update: DefectUpdate) -> Defect:
    
    for i, defect in enumerate(defects):

        if defect.defectId == defectId:
            defect.status = update.status
            return defect
    
    raise HTTPException(404,f'no defect with ID {defectId} found')



@app.get("/defects", response_model=list[Defect])
def get_all_defects() -> list[Defect]:
    return defects


@app.get("/defects/{defectId}")
def get_defect_by_id(defectId: int) -> Defect:
    
    for defect in defects:
        if defect.defectId == defectId:
            return defect
    
    raise HTTPException(404,f'no defect with ID {defectId} found')


## Test Summarizer

@app.post("/projects", response_model=Project)
def create_project(project_form: ProjectForm) -> Project:
    project = Project(projectId=randint(10000,99999), **project_form.dict())
    projects.append(project)
    return project
    

@app.get("/projects", response_model=list[Project])
def get_all_projects() -> list[Project]:
    return projects

@app.get("/projects/{projectId}", response_model=Project)
def get_project_by_id(projectId: int):
    
    for project in projects:
        if project.projectId == projectId:
            return project
    else:
        raise HTTPException(404,f'no project with ID {projectId} found' )



@app.post("/summaries",  response_model=TestSummary, status_code=201)
def create_test_summary(summary_form: TestSummaryForm) -> TestSummary:
    
    summary = TestSummary(summaryId=randint(10000,99999), **summary_form.dict(), isFinalized=False)

    for project in projects:

        if project.projectId == summary.projectId:
            summaries.append(summary)
            return summary

    else:
        raise HTTPException(404,f'no project with id {summary.projectId} found')



@app.get("/summaries", response_model=list[TestSummary])
def get_all_summaries() -> list[TestSummary]:
    return summaries


@app.get("/summaries/{summaryId}", response_model=TestSummary)
def get_summary_by_id(summaryId: int) -> TestSummary:
    
    for summary in summaries:
        if summary.summaryId == summaryId:
            return summary
    else:
        raise HTTPException(404, f'no Test Summary with id {summaryId} found')


@app.get("/cases", response_model=list[TestCase])
def get_cases(summaryId: int | None = None):
    
    if summaryId:
        return [c for c in cases if c.summaryId == summaryId]
    else:
        return cases



@app.post("/cases", response_model=TestCase, status_code=201)
def create_test_case(case_form: TestCaseForm) -> TestCase:
    
    case = TestCase(caseId=randint(10000,99999), **case_form.dict())

    for summary in summaries:

        if summary.summaryId == case.summaryId:
            cases.append(case)
            return case
    else:
        raise HTTPException(404, f'No Summary found with id {case.summaryId}')


@app.delete("/cases/{caseId}" ,status_code=204)
def delete_test_case(caseId: int):
    
    for i, case in enumerate(cases):
        
        if case.caseId == caseId:
            del cases[i]
            break

    else:
        raise HTTPException(404, f'no case with id {caseId} found')


## debug routes
@app.get('/debug/appstate')
def everything():
    return {"employees":employees, "defects":defects, "projects":projects, "summaries":summaries, "test cases":cases }


@app.delete('/debug/nuke', status_code=204)
def destroy_all():
    employees.clear()
    defects.clear()
    projects.clear()
    summaries.clear()
    cases.clear()