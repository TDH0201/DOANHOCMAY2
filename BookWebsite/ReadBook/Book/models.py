from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class MyUser(AbstractUser):
    lastUpdate = models.DateTimeField(auto_now=True)
    lastUpdater = models.CharField(max_length=255, default='')
    createdDate = models.DateTimeField(auto_now_add=True)
    createdDater = models.CharField(max_length=255, default='')


class MyBase(models.Model):
    lastUpdate = models.DateTimeField(auto_now_add=True, null=True)
    lastUpdater = models.CharField(max_length=255, default='', null=True)
    createdDate = models.DateTimeField(auto_now=True, null=True)
    createdDater = models.CharField(max_length=255, default='', null=True)

    class Meta:
        abstract = True


class Author(MyBase):
    authorName = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=255, default='SOME STRING')
    email = models.CharField(max_length=255, default='SOME STRING')
    emailChecked = models.BooleanField(default=True)

    def __str__(self):
        return self.authorName


class Book(MyBase):
    ISBN = models.CharField(max_length=14, default='SOME STRING')
    bookName = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, default='SOME STRING', null=True)
    contents = models.CharField(max_length=255, default='SOME STRING', null=True)
    overview = models.CharField(max_length=255, default='SOME STRING', null=True)
    imgBook = models.CharField(max_length=255, default='SOME STRING')
    imgBookM = models.CharField(max_length=255, default='SOME STRING')
    imgBookL = models.CharField(max_length=255, default='SOME STRING')
    Auth = models.CharField(max_length=255, default='SOME STRING')
    ratingCount = models.IntegerField(default=0, null=True)
    Publisher = models.CharField(max_length=255, default='SOME STRING')
    YearOfPublication = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="author",
                               null=True, blank=True)
    user = models.ManyToManyField(MyUser)
    average_rating = models.FloatField(default=0, null=True)
    num_pages = models.IntegerField(default=0, null=True)
    text_reviews_count = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.bookName


class ActionBase(models.Model):
    createdDate = models.DateTimeField(auto_now_add=True,  null=True)
    lastUpdate = models.DateTimeField(auto_now=True,  null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    creator = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Action(ActionBase):
    Like, Heart = range(2)
    ACTIONS = [
        (Like, 'like'),
        (Heart, 'heart')
    ]
    type = models.PositiveSmallIntegerField(choices=ACTIONS, default=Like)


class Rating(ActionBase):
    rate = models.PositiveSmallIntegerField(default=0)


class Comment(ActionBase):
    content = models.TextField()

    def __str__(self):
        return self.content
