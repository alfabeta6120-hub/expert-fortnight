from django.urls import path,include
from rest_framework.routers import DefaultRouter
from books.views import AuthorViewSet,GenreViewSet,BookTypeViewSet,BookViewSet

router = DefaultRouter()
router.register('Author',AuthorViewSet)
router.register('Genre',GenreViewSet)
router.register('BookType',BookTypeViewSet)
router.register('Book',BookViewSet)

urlpatterns = [
    path("",include(router.urls))
]