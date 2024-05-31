from .base import BaseRepository


class CityRepository(BaseRepository):
    def __init__(self):
        super().__init__("cities")

