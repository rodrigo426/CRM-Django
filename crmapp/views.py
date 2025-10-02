from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def home(request):
    #Verificar login
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        #Autenticação
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login realizado com sucesso!")
            return redirect('home')
        else:
            messages.success(request, "Login sem sucesso, tente novamente!")
            return redirect('home')
    else:
        return render (request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "Logout realizado.")
    return redirect('home')