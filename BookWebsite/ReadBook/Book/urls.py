from rest_framework import routers
from .views import BookViewSet, AuthorViewSet,BookDetailViewSet, AuthInfo, UserRegisterView, Bookjson
from django.urls import path, include


router = routers.DefaultRouter()
router.register('Book', BookViewSet, 'Book')
router.register('Auhthor', AuthorViewSet, 'Author')
router.register("book-detail", BookDetailViewSet, 'book_Detail')
router.register("user", UserRegisterView, "user-register")

urlpatterns = [
    path('', include(router.urls)),
    path('oauth2-info/', AuthInfo.as_view()),
    path('bookjson/', Bookjson.as_view()),
]
