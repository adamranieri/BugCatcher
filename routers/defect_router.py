from random import randint
from fastapi import APIRouter, HTTPException


from models.defect_models import Defect, DefectForm, DefectUpdate
from models.enums import DefectStatus, Level

from . import employee_router

router = APIRouter()

defects: list[Defect] = [
    Defect(defectId=101, assignedTo="Sierra117", dateReported=10000, status=DefectStatus.PENDING, severity=Level.LOW, priority=Level.HIGH, desc="Sample", stepsToReproduce="1. does not actually exist"),
    Defect(defectId=202, assignedTo="ryan99", dateReported=10000, status=DefectStatus.ACCEPTED, severity=Level.LOW, priority=Level.HIGH, desc="ultra bug", stepsToReproduce="1. something")
    ]


@router.post("/defects", response_model=Defect, status_code=201)
def create_defect(defect_form: DefectForm) -> Defect:
    defect = Defect(defectId=randint(10000,99999), **defect_form.dict(), status=DefectStatus.PENDING)
    defects.append(defect)
    return defect

@router.put("/defects")
def replace_defect(defect:Defect)->Defect:
    for i, d in enumerate(defects):
        if d.defectId == defect.defectId:
            defects[i] = defect
            return defect
    else:
        raise HTTPException(404,f'no defect found with id {defect.defectId}')


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

