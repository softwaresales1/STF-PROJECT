from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render

def get_started(request):
    return render(request, 'Portal/get_started.html')

def home(request):
    return render(request, 'Portal/home.html')

def services(request):
    return render(request, 'Portal/services.html')

def contactus(request):
    return render(request, 'Portal/contactus.html')

def join_wait_list(request):
    return render(request, 'Portal/join_wait_list.html')

def check_username(request):
    # Logic to check if the username exists
    return render(request, 'Portal/check_username.html')

def check_email(request):
    # Logic to check if the email exists
    return render(request, 'Portal/check_email.html')

def auth_callback_token(request, token):
    # Logic to handle the authentication callback with the token
    return render(request, 'Portal/auth_callback_token.html')

def login_user(request):
    # Logic for user login
    return render(request, 'Portal/login.html')

def logout_user(request):
    # Logic for user logout
    return render(request, 'Portal/logout.html')

def open_close_project(request):
    # Logic for opening or closing a project
    return render(request, 'Portal/open_close_project.html')

from django.contrib.auth.models import User
from django.contrib import messages

def signup(request):  
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['passwd1']
        password2 = request.POST['passwd2']
        email = request.POST['email']
        bio = request.POST['bio']

        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('Portal:signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('Portal:signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('Portal:signup')

        user = User.objects.create_user(username=username, password=password1, email=email)
        user.save()
        messages.success(request, "Account created successfully! You can now log in.")
        return redirect('Portal/index.html')

    return render(request, 'Portal/signup.html')
