from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login
from django.contrib import messages

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

        return redirect('AppCoderInicio')

    ctx = {
        'form': AuthenticationForm(),
        'name_submit': 'Login'
    }

    return render(request, 'userapp/login.html', ctx)
