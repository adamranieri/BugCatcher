from pydantic import BaseModel

from models.enums import DefectStatus, Level


class Defect(BaseModel):
    defectId: int 
    assignedTo: str | None
    dateReported: int

    status: DefectStatus
    desc: str 
    stepsToReproduce: str 
    severity: Level
    priority: Level 

class DefectForm(BaseModel):
    assignedTo: str | None
    dateReported: int
    desc: str 
    stepsToReproduce: str 
    severity: Level
    priority: Level

class DefectUpdate(BaseModel):
    status: DefectStatus