from datetime import datetime


from django.shortcuts import render,redirect
from webapp.forms import PostForm, SearchPost
from webapp.models import Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'webapp/home.html')

@login_required
def post_form(request):
    if request.method == 'POST':
        form=PostForm(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data
            new_post=Post(
                title=data.get('titulo'),
                subtitle=data.get('subtitulo'),
                content=data.get('contenido'),
                image=data.get('foto'),
                date= datetime.now(),
                author=request.user.username
                )
            
            new_post.save()

            return redirect('all_posts')


    ctx= {'form':PostForm}

    return render(request,'webapp/post_form.html',ctx)
    
def all_posts(request):
   
   post= Post.objects.all()
   ctx={'post': post}

   return render(request, 'webapp/pages.html',ctx)

def find_post(request):

    ctx={ 'form':SearchPost() }

    return render(request,'webapp/find_post.html',ctx )

def found_posts(request):

    titulo=request.GET.get('buscar')

    posts= Post.objects.filter(title__icontains=titulo)
    ctx = { 'posts' : posts }

    return render(request, 'webapp/pages.html',ctx)

def del_post(request, post_id):
    post= Post.objects.get(id = post_id)
    post.delete()
    messages.info(request, f"El post número {post_id}, fue eliminado")

    return redirect('all_posts')


def edit_post(request, post_id):
    
    post= Post.objects.get(id=post_id)


    if request.method == 'POST':
        form=PostForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            
            Post.objects.filter(id=post_id).update(
            title=data.get('titulo'),
            subtitle=data.get('subtitulo'),
            content=data.get('contenido'),
            date=datetime.now()
            ) 
            
            messages.info(request, f"El post número {post_id}, fue editado")

            return redirect('all_posts')
    
    ctx={'form':PostForm(initial={'titulo': post.title, 'subtitulo':post.subtitle,
               'contenido': post.content
                }
            )}
        


    return render(request,'webapp/update_form.html', ctx)

def read_more(request, post_id):
    post=Post.objects.get(id=post_id)

    ctx={
        'id' : post.id,
        'title': post.title,
        'content': post.content,
        'image' : post.image,
        'date': post.date
    }

    return render(request, 'webapp/post.html', ctx)
    
def read_me(request):
    return render(request, 'webapp/readme.md')

def about_me(request):
    return render(request, 'webapp/about.html')
