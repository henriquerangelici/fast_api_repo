from sqlalchemy import select

from fast_api.models import User


def test_create_user(session):
    user = User(username='henrique', email='henrique@email.com', password='senha')
    session.add(user)
    session.commit()
    result = session.scalar(select(User).where(User.email == 'henrique@email.com'))

    assert result.username == 'henrique'
