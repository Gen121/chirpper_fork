import datetime

from domain.models import Chirp, User


def test_create_chirp():
    now = datetime.datetime.now()
    user = User('sanch0', 'Sanya')
    chirp = Chirp(
        author=user,
        text='Hello',
        replies=[],
        publish_date=now
    )
    assert chirp.author == user
    assert chirp.text == 'Hello'
    assert chirp.replies == []
    assert chirp.publish_date == now


def test_create_user():
    user = User('sanch0', 'Sanya')
    assert user.login == 'sanch0'
    assert user.name == 'Sanya'
