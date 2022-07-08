from fastapi import APIRouter, HTTPException, Header
from random import randint
from models.enums import TestResult

from models.test_documents import TestCase, TestCaseForm

router = APIRouter()

cases: list[TestCase] = [
    TestCase(
        caseId=801, 
        desc="validate customers can redeem only single coupon",
        steps="1. Go to checkout page 2. click redeem on eligible coupon. 3. verify that all other redeem buttons are grayed out",
        result=TestResult.PASS,
        performedBy="ryeGuy",
        isAutomated=True,
        resultSummary="No issues"
    ),
    TestCase(
        caseId=802, 
        desc="Employees can cancel tickets when logged in",
        steps="1. log in as employee, 2. go to customer's flight iternary page, 3. click on flight. 4. press cancel and confir,",
        result=TestResult.FAIL,
        performedBy="ryeGuy",
        isAutomated=False,
        resultSummary="Can login with old password if provided valid username"
    ),
    TestCase(
        caseId=803, 
        desc="Send a photo larger than 800px  by 880px",
        steps="1. go to contact enviromentalist page. 2. send photo 3. select a large 1000px by 1000px phot",
        result=TestResult.PASS,
        performedBy=None,
        isAutomated=False,
        resultSummary="No isses in sending large photos"
    ),
    TestCase(
        caseId=804, 
        desc="Sample photos to see if they are of the correct size",
        steps="1. visit each page, 2. select 5 pictures at random, 3. compare with orginial images stored on the S3 bucet ",
        result=TestResult.FAIL,
        performedBy="cavalier89",
        isAutomated=False,
        resultSummary="Photos are badly cropped. Reported defect"
    ),

]

@router.post("/cases", response_model=TestCase, status_code=201)
def add_test_case(case_form: TestCaseForm, dev: str = Header(default="0")) -> TestCase:
    case = TestCase(caseId=randint(10000,99999), **case_form.dict())
    cases.append(case)
    return case

@router.put("/cases/{caseId}")
def update_test_case(test_case:TestCase, caseId: int, dev: str = Header(default="0")) -> TestCase:

    for i, case in enumerate(cases):
        if case.caseId == caseId:
            cases[i] = test_case
            return test_case
    else:
        raise HTTPException(404,f'No Cases with id {caseId} found')

@router.get("/cases")
def get_all_test_cases(dev: str = Header(default="0")) -> list[TestCase]:
    return cases

@router.get("/cases/{caseId}")
def get_case_by_id(caseId: int, dev: str = Header(default="0")) -> TestCase:

    for case in cases:
        if case.caseId == caseId:
            return case 
    else:
        raise HTTPException(404,f'no test case with id {caseId} found')