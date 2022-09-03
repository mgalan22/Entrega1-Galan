from datetime import datetime
from django.shortcuts import render,redirect
from webapp.forms import PostForm, SearchPost
from webapp.models import Posts


def home(request):
    return render(request, 'webapp/home.html')

def post_form(request):
    if request.method == 'POST':
        formulario=PostForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            post1=Posts(title=data.get('titulo'),content=data.get('contenido'), date= datetime.now())
            post1.save()

            return redirect('all_posts')


    ctx= {'form':PostForm}

    return render(request,'webapp/post_form.html',ctx)
    
def all_posts(request):
   
   posts= Posts.objects.all()
   ctx={'posts': posts}

   return render(request, 'webapp/all_posts.html',ctx)

def find_post(request):

    ctx={ 'form':SearchPost() }

    return render(request,'webapp/find_post.html',ctx )

def found_posts(request):

    titulo=request.GET.get('buscar')

    posts= Posts.objects.filter(title__icontains=titulo)
    ctx = { 'posts' : posts }

    return render(request, 'webapp/all_posts.html',ctx)


def read_me(request):
    return render(request, 'webapp/readme.md')



def edit_post(request):
    pass
    return render(request)

def del_post(request):
    pass
    return render(request)

def read_more(request):
    pass
    return render(request)

def new_user(request):
    pass
    return render(request)