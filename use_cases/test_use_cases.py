import datetime

from domain.models import Chirp, User
from repository.db import MockDb
from use_cases.use_cases import ChirpHandler


def test_create_chirp():
    now = datetime.datetime.now()
    user = User('sanch0', 'Sanya')
    chirp = Chirp(
        author=user,
        text='Hello',
        replies=[],
        publish_date=now
    )
    uuid = chirp.uuid

    db = MockDb()
    chirp_handler = ChirpHandler(db)

    chirp_handler.create_chirp(chirp)
    chirp_from_db = db.read_chirp_from_db(uuid)

    assert chirp_from_db.uuid == uuid


def test_reply_chirp():
    now = datetime.datetime.now()
    user = User('sanch0', 'Sanya')
    chirp1 = Chirp(
        author=user,
        text='Hello',
        replies=[],
        publish_date=now
    )
    chirp2 = Chirp(
        author=user,
        text='Hello',
        replies=[],
        publish_date=now
    )
    uuid1 = chirp1.uuid
    uuid2 = chirp2.uuid

    db = MockDb()
    chirp_handler = ChirpHandler(db)

    chirp_handler.reply_chirp(chirp1, chirp2)
    chirp_from_db1 = db.read_chirp_from_db(uuid1)
    chirp_from_db2 = db.read_chirp_from_db(uuid2)

    assert chirp_from_db2 in chirp_from_db1.replies
    assert chirp_from_db2.parent == chirp_from_db1
