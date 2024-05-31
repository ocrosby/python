from .base import BaseRepository


class CountryRepository(BaseRepository):
    def __init__(self):
        super().__init__("countries")

