import pytest
from django.contrib.auth import get_user_model


@pytest.mark.django_db
def test_create_user():
    User = get_user_model()
    user = User.objects.create_user(email='test2@admin.com', fullname='Test User', password='TestPass123')
    users = User.objects.all()
    assert len(users) == 2

# @pytest.mark.django_db
# def test_create_user(user, django_user_model):
#     users = django_user_model.objects.all()
#     assert len(users) == 2

# @pytest.mark.skipif(reason='WIP')
@pytest.mark.smoke
@pytest.mark.slow
def test_change_password(user):
    user.set_password('secret')
    assert user.check_password('secret') is True

