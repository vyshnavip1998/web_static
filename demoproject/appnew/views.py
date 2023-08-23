from django.contrib import messages, auth
from django.contrib.auth.models import User
# from django.core.checks import messages
from django.shortcuts import render, redirect


# Create your views here.
# login code
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid Response ! Please enter correct username and password")
            return redirect('login')

    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpass = request.POST['password1']
        if password == cpass:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Already Existed")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                email=email, password=password)
                user.save();
                return redirect('login')
            # print("USER CREATED")

        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('/')
    return render(request, "registration.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
