from django.shortcuts import render
from  django.views import View

# Create your views here.
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

class DetailBook(View):
    def get(self, request):
        return render(request, 'detail.html')
