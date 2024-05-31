from fastapi import APIRouter
from microservices.location.repository.postal_code import PostalCodeRepository

router = APIRouter()


@router.get("/postal_codes")
async def get_postal_codes():
    repo = PostalCodeRepository()
    return repo.find_all()


@router.get("/postal_codes/{id}")
async def get_postal_code(id: int):
    repo = PostalCodeRepository()
    return repo.find_by_id(id)


@router.post("/postal_codes")
async def create_postal_code(data: dict):
    repo = PostalCodeRepository()
    return repo.create(data)


@router.put("/postal_codes/{id}")
async def update_postal_code(id: int, data: dict):
    repo = PostalCodeRepository()
    return repo.update(id, data)


@router.delete("/postal_codes/{id}")
async def delete_postal_code(id: int):
    repo = PostalCodeRepository()
    return repo.delete(id)

# Path: microservices/location/repository/postal_code_routes.py
