from django.contrib import messages
from django.contrib.auth.models import auth, User
from django.shortcuts import render, redirect


def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')
def register(request):
    if request.method=="POST":
        first_name=request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        confirm_password = request.POST['confirm password']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username  taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email  taken")
                return redirect('register')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                user.save();
                print("user created")
        else:
            print("Password not matched")
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'sign_up.html')
def logout(request):
    auth.logout(request)
    return  redirect('/')


# Create your views here.

# Create your views here.
