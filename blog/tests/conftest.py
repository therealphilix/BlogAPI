from django.contrib.auth.models import User
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
import pytest

from blog.models import Author, Category

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def authenticate(api_client):
    def do_authenticate(is_staff=False):
        return api_client.force_authenticate(user=User(is_staff=is_staff))
    return do_authenticate

@pytest.fixture
def authenticate_one(api_client):
    def do_authenticate(user):
        return api_client.force_authenticate(user=user)
    return do_authenticate

@pytest.fixture
def user():
    User = get_user_model()
    return User.objects.create(username='indie', password='testpassword', 
                               email='indie@domain.com', first_name='testname', last_name='testname2')

@pytest.fixture
def author(user):
    return Author.objects.create(phone='+2349012012573', user=user.id)

@pytest.fixture
def category():
    return Category.objects.create(title='tech', slug='-')
    