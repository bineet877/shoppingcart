import email
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.


def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        emailId = request.POST['email_id']
        password = request.POST['password']
        username = request.POST['email_id']
        user = User.objects.create_user(username = username,password=password,first_name=first_name,last_name=last_name,email=emailId)
        user.save()
        print('User created')
        return redirect("/")
    else:
        return render(request,"register.html")


def logout_user(request):
    logout(request)
    return redirect("login")

def login_user(request):
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['pass']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return redirect("register")
    else:
        return render(request,"login.html")

    