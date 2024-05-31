from fastapi import APIRouter
from microservices.location.repository.location import LocationRepository

router = APIRouter()


@router.get("/locations")
async def get_locations():
    repo = LocationRepository()
    return repo.find_all()


@router.get("/locations/{id}")
async def get_location(id: int):
    repo = LocationRepository()
    return repo.find_by_id(id)


@router.post("/locations")
async def create_location(data: dict):
    repo = LocationRepository()
    return repo.create(data)


@router.put("/locations/{id}")
async def update_location(id: int, data: dict):
    repo = LocationRepository()
    return repo.update(id, data)


@router.delete("/locations/{id}")
async def delete_location(id: int):
    repo = LocationRepository()
    return repo.delete(id)

# Path: microservices/location/repository/location_routes.py
