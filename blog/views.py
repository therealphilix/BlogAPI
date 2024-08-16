from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *
from .pagination import DefaultPagination
from .filters import PostFilter
# Create your views here.

class PostViewSet(ModelViewSet):
    queryset = Post.objects.select_related('category', 'author').all()
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = PostFilter
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return UpdatePostSerializer
        return PostSerializer
    
    # def get_serializer_context(self):
    #     context = super().get_serializer_context()
    #     user = self.request.user
    #     if user.is_authenticated:
    #         author = Author.objects.get(user_id=user.id)
    #         context['author_id'] = author.id
    #     return context

    # def get_serializer_context(self):
    #     author = Author.objects.get(user_id=self.request.user.id)
    #     return {'author_id': author.id}
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        try:
            author = Author.objects.get(user_id=self.request.user.id)
        except Author.DoesNotExist:
            author = None  # Handle this scenario appropriately
        context['author'] = author
        return context

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminUser]

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        author = Author.objects.get(
            user_id=request.user.id
        )
        if request.method == 'GET':
            serializer = AuthorSerializer(author)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = AuthorSerializer(author, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)


class CategorViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['post_pk'])

    def get_serializer_context(self):
        author = Author.objects.get(user_id=self.request.user.id)
        return {'post_id': self.kwargs['post_pk'], 'author_id': author.id}