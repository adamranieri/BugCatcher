from fastapi import APIRouter, HTTPException
from random import randint
from models.enums import TestResult

from models.test_documents import TestCase, TestCaseForm

router = APIRouter()

cases: list[TestCase] = [
    TestCase(
        caseId=20001, 
        desc="validate customers can redeem only single coupon",
        steps="1. Go to checkout page 2. click redeem on eligible coupon. 3. verify that all other redeem buttons are grayed out",
        result=TestResult.PASS,
        performedBy="ryan99",
        isAutomated=True,
        resultSummary="No issues"
    ),
    TestCase(
        caseId=20002, 
        desc="old passwords cannot be used",
        steps="1. go to login page, 2. entered expired but valid username password",
        result=TestResult.FAIL,
        performedBy="Sierra117",
        isAutomated=False,
        resultSummary="Can login with old password if provided valid username"
    ),
    TestCase(
        caseId=20003, 
        desc="Employees can change their username",
        steps="1. go to my settings page, 2. click update username, 3. enter new username, 4. submit 5 verify that login is possible with new username ",
        result=TestResult.UNEXECUTED,
        performedBy=None,
        isAutomated=False,
        resultSummary=None
    ),
]

@router.post("/cases", response_model=TestCase, status_code=201)
def add_test_case(case_form: TestCaseForm) -> TestCase:
    case = TestCase(caseId=randint(10000,99999), **case_form.dict())
    cases.append(case)
    return case

@router.put("/cases/{caseId}")
def update_test_case(test_case:TestCase, caseId: int) -> TestCase:

    for i, case in enumerate(cases):
        if case.caseId == caseId:
            cases[i] = test_case
            return test_case
    else:
        raise HTTPException(404,f'No Cases with id {caseId} found')

@router.get("/cases")
def get_all_test_cases() -> list[TestCase]:
    return cases

@router.get("/cases/{caseId}")
def get_case_by_id(caseId: int) -> TestCase:

    for case in cases:
        if case.caseId == caseId:
            return case 
    else:
        raise HTTPException(404,f'no test case with id {caseId} found')