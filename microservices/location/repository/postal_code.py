from .base import BaseRepository


class PostalCodeRepository(BaseRepository):
    def __init__(self):
        super().__init__("postal_codes")

