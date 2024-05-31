from fastapi import APIRouter
from microservices.location.repository.country import CountryRepository

router = APIRouter()


@router.get("/countries")
async def get_countries():
    repo = CountryRepository()
    return repo.find_all()


@router.get("/countries/{id}")
async def get_country(id: int):
    repo = CountryRepository()
    return repo.find_by_id(id)


@router.post("/countries")
async def create_country(data: dict):
    repo = CountryRepository()
    return repo.create(data)


@router.put("/countries/{id}")
async def update_country(id: int, data: dict):
    repo = CountryRepository()
    return repo.update(id, data)


@router.delete("/countries/{id}")
async def delete_country(id: int):
    repo = CountryRepository()
    return repo.delete(id)

# Path: microservices/location/repository/country_routes.py
