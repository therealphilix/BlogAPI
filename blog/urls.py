from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('posts', views.PostViewSet)
router.register('authors', views.AuthorViewSet)
router.register('category', views.CategorViewSet)

posts_router = routers.NestedDefaultRouter(
    router, 'posts', lookup='post'
)
posts_router.register(
    'comments', views.CommentViewSet,
    basename='post-comments'
)

urlpatterns = router.urls + posts_router.urls