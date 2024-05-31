from fastapi import APIRouter
from microservices.location.repository.state import StateRepository

router = APIRouter()


@router.get("/states")
async def get_states():
    repo = StateRepository()
    return repo.find_all()


@router.get("/states/{id}")
async def get_state(id: int):
    repo = StateRepository()
    return repo.find_by_id(id)


@router.post("/states")
async def create_state(data: dict):
    repo = StateRepository()
    return repo.create(data)


@router.put("/states/{id}")
async def update_state(id: int, data: dict):
    repo = StateRepository()
    return repo.update(id, data)


@router.delete("/states/{id}")
async def delete_state(id: int):
    repo = StateRepository()
    return repo.delete(id)

# Path: microservices/location/repository/state_routes.py
