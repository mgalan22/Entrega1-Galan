from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from userapp.forms import *
from django.contrib.auth.decorators import login_required


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
            messages.info(request, 'Error de registro, los datos no se guardaron')
        
        return redirect('/')

    ctx = {
        'form': UserRegisterForm(),
        'nombre_form': 'Registro'
    }

    return render(request, 'userapp/login.html', ctx)

@login_required
def user_edit(request):
    user = request.user
    
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():
            
            data = form.cleaned_data

            user.username = data.get('username')
            user.email = data.get('email')
            user.first_name = data.get('first_name')
            user.last_name = data.get('last_name')

            user.save()


            messages.info(request, 'Usuario registrado satisfactoriamente!')
        
        else:
            messages.info(request, 'Error de registro, los datos no se guardaron')
        
        return redirect('/')
    
    
    ctx = {
        'form': UserRegisterForm(
            initial={
                'username':user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name
                
                 }),
        'nombre_form': 'Actualizar perfil'
    }

    return render(request, 'userapp/login.html', ctx)

@login_required
def upload_avatar(request):
    if request.method == "POST":

        form = AvatarForm(request.POST, request.FILES)

        if form.is_valid():

            data = form.cleaned_data
            avatar = Avatar.objects.filter(user=data.get("user"))

            if len(avatar) > 0:
                avatar = avatar[0]
                avatar.image = form.cleaned_data["image"]
                avatar.save()

            else:
                avatar = Avatar(user=data.get("user"), image=data.get("image"))
                avatar.save()

        return redirect('home')

    ctx = {
        "form": AvatarForm(),
        "nombre_form" : 'Subir imagen'
    }

    return render(request, "userapp/login.html", ctx)