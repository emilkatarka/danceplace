import pytest


@pytest.fixture(scope='function')
def user(db, django_user_model):
    yield django_user_model.objects.create_user(email='test2@admin.com', fullname='Test User', password='TestPass123')
