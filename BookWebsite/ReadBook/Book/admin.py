from django.contrib import admin
from .models import Book, Author, MyUser, Rating, Action
# Register your models here.

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(MyUser)
admin.site.register(Rating)
admin.site.register(Action)
