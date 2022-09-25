from datetime import datetime

from django.shortcuts import render,redirect
from webapp.forms import PostForm, SearchPost
from webapp.models import Posts
from django.contrib import messages


def home(request):
    return render(request, 'webapp/home.html')

def post_form(request):
    if request.method == 'POST':
        formulario=PostForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            new_post=Posts(title=data.get('titulo'),content=data.get('contenido'), date= datetime.now())
            new_post.save()

            return redirect('all_posts')


    ctx= {'form':PostForm}

    return render(request,'webapp/post_form.html',ctx)
    
def all_posts(request):
   
   posts= Posts.objects.all()
   ctx={'posts': posts}

   return render(request, 'webapp/pages.html',ctx)

def find_post(request):

    ctx={ 'form':SearchPost() }

    return render(request,'webapp/find_post.html',ctx )

def found_posts(request):

    titulo=request.GET.get('buscar')

    posts= Posts.objects.filter(title__icontains=titulo)
    ctx = { 'posts' : posts }

    return render(request, 'webapp/pages.html',ctx)

def del_post(request, id):
    post_del = Posts.objects.get(id=id)
    post_del.delete()
    messages.info(request, f"El post número {id}, fue eliminado")

    return redirect('all_posts')

def edit_post(request, post_id):
    
    post_to_edit= Posts.objects.get(id=post_id)


    if request.method == 'POST':
        formulario=PostForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            
            Posts.objects.filter(id=post_id).update(
            title=data.get('titulo'),
            content=data.get('contenido'),
            date=datetime.now()
            ) 
            
            messages.info(request, f"El post número {post_id}, fue editado")

            return redirect('all_posts')
    
    ctx={'form':PostForm(initial={'titulo': post_to_edit.title,
               'contenido': post_to_edit.content
                }
            )}
        


    return render(request,'webapp/update_form.html', ctx)


    
def read_me(request):
    return render(request, 'webapp/readme.md')

def read_more(request):
    pass
    return render(request)

def new_user(request):
    pass
    return render(request)