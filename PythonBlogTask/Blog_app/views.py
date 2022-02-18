from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from . models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import PostForm, EditForm

# Create your views here.


# def home(request):
#     return render(request, "blogapp/homepage.html")

def signup(request):
    if request.method == 'POST' :
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username")
            return redirect('home')

        if User.objects.filter(email=email):
            messages.error(request, "Email already registered")
            return redirect('home')
        
        if len(username)>15:
            messages.error(request, "Username must be under 10 characters")

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!")

        if pass1 != pass2:
            messages.error(request, "Passwords didn't match!")
            return redirect('home')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
  
        myuser.save()

        # messages.success(request, "Your account has been successfully created")

        return redirect('signin')

    return render(request, "blogapp/signup.html")



def signin(request):

    if request.method == 'POST' :
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return redirect('home')
            
            # return render(request, "blogapp/homepage.html", {'fname': fname})
            

        else:
            messages.error(request, "Bad Credentials")
            return redirect('home')

    return render(request, "blogapp/signin.html")

def signout(request):
    logout(request)
    # messages.success(request, "Logged Out Successfully!")
    return redirect('home')


# class Listview2(ListView):
#     model = Post
#     template_name = "blogapp/loginhomepage.html"

class Listview(ListView):
    model = Post
    template_name = 'blogapp/homepage.html'
    ordering = ['-post_date']

class blogdetails(DetailView):
    model = Post
    template_name = 'blogapp/blogdetails.html'

class addblog(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blogapp/addblog.html'
    # fields = '__all__'

class editblog(UpdateView):
    model = Post 
    form_class = EditForm
    template_name = 'blogapp/editblog.html'
    # fields = ['title', 'body']

class deleteblog(DeleteView):
    model = Post
    template_name = 'blogapp/deleteblog.html'
    success_url = reverse_lazy('home')

class myblogs(ListView):
    model = Post
    template_name = 'blogapp/myblogs.html'
    # ordering = ['-id']
    
def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        searchresults = Post.objects.filter(title__contains=searched)
        return render(request, 'blogapp/search.html', {'searched':searched, 'searchresults': searchresults})
    else:
        return render(request, 'blogapp/search.html', {})
