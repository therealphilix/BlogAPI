from rest_framework.test import APIClient
from rest_framework import status
from model_bakery import baker
from blog.models import Post, Author, Category
from django.contrib.auth import get_user_model
import pytest

@pytest.mark.django_db
class TestCreatePost:
    User = get_user_model()
    def test_if_user_is_anonymous_returns_401(self, api_client):
        response = api_client.post('/blog/posts/', {'title': 'this siiiajpoe', 'slug': '-'})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_data_is_invalid_returns_400(self, api_client, authenticate):
        authenticate(is_staff=True)
        response = api_client.post('/blog/posts/', {'title': ''})
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None

    def test_if_data_is_valid_returns_200(self, api_client, authenticate_one, user, author, category):
        authenticate_one(user)
        response = api_client.post('/blog/posts/', {'title': 'a',
                                                    'content': 'didifhe',
                                                    'author': author.id,
                                                    'category': category.id,
                                                    'status': 'draft'})
        assert response.status_code == status.HTTP_200_OK

