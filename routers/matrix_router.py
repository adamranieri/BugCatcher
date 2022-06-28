from fastapi import APIRouter, HTTPException
from models.matrix_models import Matrix, MatrixForm, Requirement
from random import randint

router = APIRouter()

matrices: list[Matrix] = []

@router.post("/matrices", response_model=Matrix)
def create_matrix(matrix_form: MatrixForm) -> Matrix:
    matrix = Matrix(matrixId=randint(10000,99999), **matrix_form.dict())
    matrices.append(matrix)
    return matrix


@router.put("/matrices/{matrixId}/requirements")
def update_requirements(requirements:list[Requirement], matrixId: int) -> Matrix:
    
    for matrix in matrices:
        if matrix.matrixId == matrixId:
            matrix.requirements = requirements
    else:
        raise HTTPException(404,f'no matrix with id {matrixId} found')


@router.get("/matrices", response_model=list[Matrix])
def get_all_matrices()-> list[Matrix]:
    return matrices






