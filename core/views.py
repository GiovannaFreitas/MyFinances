from django.shortcuts import render
from .models import *
from .forms import UsuariosForm
# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def one(request):
    return render(request, 'page-one.html')


def poupanca(request):
    return render(request, 'poupanca.html')


def create(request):
    if request.method == "POST":
        form = UsuariosForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UsuariosForm()
    return render(request, 'create.html', {'form': form})
