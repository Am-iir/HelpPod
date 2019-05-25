from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


from django.contrib.auth import (
     authenticate, 
     get_user_model,
     login,
     logout,
)

from .forms import UserLoginForm , TaskForm ,UserSignUpForm ,HelperForm
from .models import Task



# Create your views here.

def home(request):
    return render(request,"home.html",{})

def login_view(request):
    title="Login"
    form = UserLoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form. cleaned_data.get('password')
        user = authenticate(username=username , password=password)
        login(request,user)
        return redirect("/")

    return render(request,"login.html",{"form":form,"title":title})


def choose_signup(request):
    return render(request,"choose_signup.html",{})


def signup_view(request):
    title="Signup"
    form = UserSignUpForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username , password=password)
        login(request,new_user)
        return redirect("login")      

    context = {
        "form":form,
        "title":title
    }

    return render(request,"signup.html",context)

    
def helpsignup_view(request):
    title="Signup"
    form = HelperForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)       
        instance.save()
        return redirect("contact")       

    context = {
        "form":form,
        "title":title
    }

    return render(request,"helper_signup.html",context)


def post_task(request):
    form = TaskForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        user_name = request.user.username
        instance.user_name=user_name
        instance.save()
        return redirect("success") 

    return render(request,"post.html",{"form":form})

def task_list(request):
    queryset_list = Task.objects.all()
    
    query=request.GET.get("q")
    if query:
        queryset_list=queryset_list.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(drop_location__icontains=query) |
            Q(pickup_location__icontains=query)
        ).distinct()

    paginator = Paginator(queryset_list, 8) # Show contacts per page
    page_request_var="page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    
    context = {
        "object_list": queryset,
        "title":"Tasks Available",
        "page_request_var":page_request_var,
    }

    return render(request,"task_list.html",context)

def task_detail(request,id=None): 

   instance =get_object_or_404(Task , id=id)
   context = {       
      "title":instance.title,
      "instance":instance
   }
   return render(request,"task_detail.html",context)

def accept(request, id=None):
    instance =get_object_or_404(Task, id=id)   
    instance.delete()   
    return redirect("hsuccess")

def success(request):
    return render(request,"success.html",{})

def helper_success(request):
    return render(request,"helper_success.html",{})

def contact_us(request):
     return render(request,"contact_us.html",{})


def logout_view(request):
    logout(request)
    return redirect("home")
    


