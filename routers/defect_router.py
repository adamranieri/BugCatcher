from random import randint
from fastapi import APIRouter, HTTPException


from models.defect_models import Defect, DefectForm, DefectUpdate
from models.enums import DefectStatus, Level

from . import employee_router

router = APIRouter()

defects: list[Defect] = [
    Defect(defectId=101, assignedTo="Billy", dateReported=10000, status=DefectStatus.PENDING, severity=Level.LOW, priority=Level.HIGH, desc="Sample", stepsToReproduce="1. does not actually exist")
    ]


@router.post("/defects", response_model=Defect, status_code=201)
def create_defect(defect_form: DefectForm) -> Defect:
    defect = Defect(defectId=randint(10000,99999), **defect_form.dict(), status=DefectStatus.PENDING)

    for emp in employee_router.employees:
        if emp.username == defect.assignedTo:
            break
    else:
        raise HTTPException(404, f'Could not find an employee with username {defect.assignedTo}')

    defects.append(defect)
    return defect



@router.patch("/defects/{defectId}", status_code=204)
def update_defect(defectId: int, update: DefectUpdate) -> Defect:
    
    for i, defect in enumerate(defects):

        if defect.defectId == defectId:
            defect.status = update.status
            return defect
    
    raise HTTPException(404,f'no defect with ID {defectId} found')



@router.get("/defects", response_model=list[Defect])
def get_all_defects() -> list[Defect]:
    return defects


@router.get("/defects/{defectId}")
def get_defect_by_id(defectId: int) -> Defect:
    
    for defect in defects:
        if defect.defectId == defectId:
            return defect
    
    raise HTTPException(404,f'no defect with ID {defectId} found')

