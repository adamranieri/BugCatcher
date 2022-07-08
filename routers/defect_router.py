from random import randint
from fastapi import APIRouter, HTTPException, Header


from models.defect_models import Defect, DefectForm, DefectUpdate
from models.enums import DefectStatus, Level

from . import employee_router

router = APIRouter()

defects: list[Defect] = [
    Defect(defectId=901, assignedTo="ryeGuy", dateReported=10000, status=DefectStatus.PENDING, severity=Level.LOW, priority=Level.HIGH, desc="Customers can buy multiple tickets and be charged once", stepsToReproduce="1. click on buy ticket 2. decline confirm purchase, 3. click on buy ticket again 4. confirm purchase. Can be repeated indefinetly "),
    Defect(defectId=902, assignedTo="ryeGuy", dateReported=10000, status=DefectStatus.ACCEPTED, severity=Level.MED, priority=Level.HIGH, desc="Customers cannot buy tickets if using Opera", stepsToReproduce="Attempt to buy ticket in Opera browser. It just hangs indefinetely"),
    Defect(defectId=903, assignedTo="No One", dateReported=10000, status=DefectStatus.PENDING, severity=Level.LOW, priority=Level.LOW, desc="Image Filtering is very poor. One can send a pitch black photo and still send it", stepsToReproduce="1. Take a picture of black piece of paper. 2. send it on the system"),
    Defect(defectId=904, assignedTo="cavalier89", dateReported=10000, status=DefectStatus.ACCEPTED, severity=Level.LOW, priority=Level.MED, desc="Pictures larger that 800px by 800px are not compressed. They have the exces pixels cut off. Could lose important details.", stepsToReproduce="1. send a picture larger than 800px by 800px")
    ]


@router.post("/defects", response_model=Defect, status_code=201)
def create_defect(defect_form: DefectForm, dev: str = Header(default="0")) -> Defect:
    defect = Defect(defectId=randint(10000,99999), **defect_form.dict(), status=DefectStatus.PENDING)
    defects.append(defect)
    return defect

@router.put("/defects")
def replace_defect(defect:Defect, dev: str = Header(default="0"))->Defect:
    for i, d in enumerate(defects):
        if d.defectId == defect.defectId:
            defects[i] = defect
            return defect
    else:
        raise HTTPException(404,f'no defect found with id {defect.defectId}')


@router.patch("/defects/{defectId}", status_code=204)
def update_defect(defectId: int, update: DefectUpdate, dev: str = Header(default="0")) -> Defect:
    
    for i, defect in enumerate(defects):

        if defect.defectId == defectId:
            defect.status = update.status
            return defect
    
    raise HTTPException(404,f'no defect with ID {defectId} found')



@router.get("/defects", response_model=list[Defect])
def get_all_defects(dev: str = Header(default="0")) -> list[Defect]:
    return defects


@router.get("/defects/{defectId}")
def get_defect_by_id(defectId: int, dev: str = Header(default="0")) -> Defect:
    
    for defect in defects:
        if defect.defectId == defectId:
            return defect
    
    raise HTTPException(404,f'no defect with ID {defectId} found')

