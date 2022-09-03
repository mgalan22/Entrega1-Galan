from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def new_user(request):
    pass
    return render(request)


def add_post(request):
    pass
    return render(request)

def del_post(request):
    pass
    return render(request)

def edit_post(request):
    pass
    return render(request)


def all_posts(request):
    return render(request, 'webbapp/all_posts.html')



def read_more(request):
    pass
    return render(request)


def about_me(request):
    pass
    return render(request)