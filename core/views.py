from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import UsuariosForm
# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(usuario)
            return redirect('page-one')
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'login.html', {'form_login': form_login})


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
