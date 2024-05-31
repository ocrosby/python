from .base import BaseRepository


class StateRepository(BaseRepository):
    def __init__(self):
        super().__init__("states")

