from typing import Union
import json
import os
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, generics, status, permissions
from rest_framework.views import APIView
from django.conf import settings
from .models import Book, Author, Action, Rating, Comment, MyUser
from .Serializes import (
    BookSerialize, AuthorSerialize, BookDetailSerialize, ActionSerialize, RateSerialize,
    UserSerializer, CommentSerialize

)


# Create your views here.


class BookViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerialize


class AuthorViewSet(viewsets.ViewSet, generics.ListAPIView):
    serializer_class = AuthorSerialize

    def get_queryset(self):
        author = Author.objects.all()

        name = self.request.query_params.get("author_name")
        if name is not None:
            author = author.filter(authorName__icontains=name)
        authorId = self.request.query_params.get("author_id")
        if authorId is not None:
            author = author.filter(id=authorId)
        return author

    @action(methods=['get'], detail=True, url_path="book")
    def get_bookof_author(self, request, pk):
        author = Author.objects.get(pk=pk)
        book = author.author.filter()

        return Response(BookSerialize(book, many=True).data, status=status.HTTP_200_OK)


class BookDetailViewSet(viewsets.ViewSet, generics.RetrieveAPIView):
    queryset = Book.objects.filter()
    serializer_class = BookDetailSerialize

    def get_permissions(self):
        if self.action in ["add_comment", "take_action", "rate"]:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    @action(methods=["post"], detail=True, url_path="like")
    def take_action(self, request, pk):
        try:
            action_type = int(request.data['type'])
        except Union[IndexError, ValueError]:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            action = Action.objects.create(type=action_type,
                                           creator=request.user,
                                           book=self.get_object())
        return Response(ActionSerialize(action).data, status=status.HTTP_200_OK)

    @action(methods=["post"], detail=True, url_path="rate")
    def rate(self, request, pk):
        try:
           rating = int(request.data['rating'])
        except Union[IndexError, ValueError]:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            rate = Rating.objects.create(rate=rating,
                                           creator=request.user,
                                           book=self.get_object())
        return Response(ActionSerialize(rate).data, status=status.HTTP_200_OK)

    @action(methods=["post"], detail=True, url_path="add_comment")
    def add_comment(self, request, pk):
        content = request.data.get("content")
        if content:
            c = Comment.objects.create(content=content, book=self.get_object(), creator=request.user)
            return Response(CommentSerialize(c).data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


# Register API
class UserRegisterView(viewsets.ViewSet, generics.CreateAPIView):
    queryset = MyUser.objects.filter(is_active=True)
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == "getUser":
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    @action(methods=['get'], detail=False, url_path="current-user")
    def getUser(self, request):
        return Response(self.serializer_class(request.user).data, status=status.HTTP_200_OK)


class AuthInfo(APIView):
    def get(self, request):
        return Response(settings.OAUTH2_INFO, status=status.HTTP_200_OK)


class Bookjson(APIView):
    def get(self, request):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(dir_path + '/' + 'book.json') as file:
            books = json.load(file)

        return Response(books, status=status.HTTP_200_OK)
