from .base import BaseRepository


class LocationRepository(BaseRepository):
    def __init__(self):
        super().__init__("locations")

