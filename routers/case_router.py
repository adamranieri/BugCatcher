from fastapi import APIRouter, HTTPException
from models.matrix_models import Matrix, MatrixForm, Requirement, TestCase
from random import randint

router = APIRouter()

cases: list[TestCase] = []

