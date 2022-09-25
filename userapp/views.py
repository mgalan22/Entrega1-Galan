from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from userapp.forms import UserRegisterForm

def login_request(request):
   
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data

            user = data.get('username')
            pwd = data.get('password')

            user = authenticate(username=user, password=pwd)

            if user:
                login(request, user)
                messages.info(request, 'Inicio de sesion satisfactorio!')

            else:
                messages.info(request, 'inicio de sesion fallido!')
        else:
            messages.info(request, 'inicio de sesion fallido!')

        return redirect('/')

    ctx = {
        'form': AuthenticationForm(),
        'nombre_form': 'Login'
    }

    return render(request, 'userapp/login.html', ctx)


def register(request):
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            form.save()

            messages.info(request, 'Usuario registrado satisfactoriamente!')
        
        else:
            messages.info(request, 'Tu usuario no puso ser registrado!')
        
        return redirect('/')

    ctx = {
        'form': UserRegisterForm(),
        'nombre_form': 'Registro'
    }

    return render(request, 'userapp/login.html', ctx)