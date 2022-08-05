from domain.models import Chirp
from repository.db import AbstractDatabase


class ChirpHandler:
    def __init__(self, db: AbstractDatabase):
        self.db = db

    def create_chirp(self, chirp: Chirp):
        self.db.save_chirp_to_db([chirp])

    def reply_chirp(self, parent_chirp: Chirp, chirp: Chirp):
        parent_chirp.replies.append(chirp)
        chirp.parent = parent_chirp
        self.db.save_chirp_to_db([parent_chirp, chirp])
