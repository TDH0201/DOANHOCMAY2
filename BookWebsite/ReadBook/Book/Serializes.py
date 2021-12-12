from rest_framework.serializers import ModelSerializer
from .models import Book, Author, Action, Rating, MyUser, Comment
from rest_framework import serializers


class AuthorSerialize(ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "authorName"]


class BookSerialize(ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "bookName", "imgBook", "Auth", "imgBookM", "imgBookL", "YearOfPublication"]


class BookDetailSerialize(BookSerialize):

    class Meta:
        model = BookSerialize.Meta.model
        fields = BookSerialize.Meta.fields + ["contents", "overview", "description"]


# Register Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = MyUser.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user


class ActionSerialize(ModelSerializer):
    class Meta:
        model = Action
        fields = ["id", "type", "creator"]


class RateSerialize(ModelSerializer):
    class Meta:
        model = Rating
        fields = ["id", "rate", "creator"]


class CommentSerialize(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "content", "createdDate", "lastUpdate"]



