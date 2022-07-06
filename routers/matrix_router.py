from fastapi import APIRouter, HTTPException
from models.enums import Level
from models.matrix_models import Matrix, MatrixForm, Requirement
from random import randint

router = APIRouter()

matrices: list[Matrix] = [
    Matrix(matrixId=60001, title="Wayne Airlines Customer Management App", 
    requirements=[
        Requirement(userStoryOrRule="As a Customer I want to buy a ticket", testCases=[10001,20002,30003], defectIds=[30001,30002,30003], priority=Level.HIGH, note="Must be done ASAP"),
        Requirement(userStoryOrRule="As an Employee cancel tickets for customers", testCases=[20005,312], defectIds=[], priority=Level.LOW, note="Customers can currently do it but most do not know how"),
        ]),
    Matrix(matrixId=60002, title="Lumber Bros Timber Lookup System", 
    requirements=[
        Requirement(userStoryOrRule="As a Lumberjack I san send pics of timber to review", testCases=[], defectIds=[3], priority=Level.LOW, note="Managers already have this feature"),
        Requirement(userStoryOrRule="All photos on the website must be at max 800px by 800px", testCases=[415,312], defectIds=[222], priority=Level.MED, note="Prohibitive Bandwidth in the field necissicates small photos"),
        ])]

@router.post("/matrices", response_model=Matrix, status_code=201)
def create_matrix(matrix_form: Matrix) -> Matrix:
    matrix = Matrix( **matrix_form.dict())
    matrix.matrixId = randint(10000,99999)
    matrices.append(matrix)
    return matrix


@router.put("/matrices/{matrixId}/requirements", response_model=Matrix)
def update_requirements(requirements:list[Requirement], matrixId: int) -> Matrix:
    
    for matrix in matrices:
        if matrix.matrixId == matrixId:
            matrix.requirements = requirements
            return matrix
    else:
        raise HTTPException(404,f'no matrix with id {matrixId} found')


@router.get("/matrices", response_model=list[Matrix])
def get_all_matrices()-> list[Matrix]:
    return matrices






