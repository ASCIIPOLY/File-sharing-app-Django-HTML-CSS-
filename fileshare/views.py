from django.shortcuts import render,redirect
from django.template import RequestContext
from django.http import HttpResponse
from .forms import AddForm
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.


def listPage(request):
    posts = Post.objects.all().order_by('-date_posted')
    context = {
        'posts':posts
    }
    return render(request, 'listpage.html',context)

def detailPage(request,pk):
    post = Post.objects.get(id=pk)
    
    
    context = {
        'post':post
    }
    return render(request, 'detailpage.html',context)



@login_required(login_url='listPage')
def newPost(request):
    current_user = request.user
    if request.method == 'POST':
        form = AddForm(request.POST, request.FILES)
 
        if form.is_valid():
            form.instance.author = request.user
            form.save()


            return redirect('/')            
    else:
        form = AddForm()
    
    context = {
        'form':form,
    }
    
    return render(request,'newPost.html',context)

@login_required(login_url='listPage')
def updatePost(request,pk):
    post = Post.objects.get(id=pk)
    form = AddForm(instance=post)
    if request.method == 'POST':
        form = AddForm(request.POST, request.FILES,instance=post)
 
        if form.is_valid():
            form.save()

            return redirect('/')            
    else:
        form = AddForm(instance=post)
    context = {
        'form':form
    }
    
    return render(request, 'update_post.html',context)

@login_required(login_url='listPage')
def deletePost(request,pk):
    post = Post.objects.get(id=pk)
   
    if request.method == 'POST':
        post.delete()

        return redirect('/')            
    
    context = {
        'post':post
    }
 
    return render(request, 'delete_post.html',context)


def myPostsPage(request):
    current_user = request.user
    post = current_user.post_set.all().order_by('-date_posted')
    
    context = {
        'posts':post
    }
    
    return render(request, 'myPosts.html',context)


def UserSpecifiedPosts(request,author):
    user = User.objects.get(username=author)
    posts = user.post_set.all().order_by('-date_posted')
    
    context = {
        'posts':posts,
        'author':author
    }
    return render(request, 'user_specified_posts.html',context)
