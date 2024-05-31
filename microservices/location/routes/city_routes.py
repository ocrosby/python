from fastapi import APIRouter
from microservices.location.repository.city import CityRepository

router = APIRouter()


@router.get("/cities")
async def get_cities():
    repo = CityRepository()
    return repo.find_all()


@router.get("/cities/{id}")
async def get_city(id: int):
    repo = CityRepository()
    return repo.find_by_id(id)


@router.post("/cities")
async def create_city(data: dict):
    repo = CityRepository()
    return repo.create(data)


@router.put("/cities/{id}")
async def update_city(id: int, data: dict):
    repo = CityRepository()
    return repo.update(id, data)


@router.delete("/cities/{id}")
async def delete_city(id: int):
    repo = CityRepository()
    return repo.delete(id)

# Path: microservices/location/repository/city_routes.py
