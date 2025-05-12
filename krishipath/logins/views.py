

from django.shortcuts import render, redirect, HttpResponse
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


# Create your views here.

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('username')        

        ''' Since built-in django takes email as authentication field, we fed it with username field but there is email 
            and obc it is working faf. ( lol )    
        '''

        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)      # authenticate the user in the database
        if user:
            login(request, user)
            return redirect('success')     # Works only for existing users; doesn't work for new users
        else:
            return HttpResponse("Invalid Credentials")
        
    return render(request, 'logins/login.html')


def user_register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            User.objects.create_user(
                username=email,
                email=email,
                password=password
            )
            return redirect('success')
        except IntegrityError:
            return HttpResponse("User already exists.")
    
    return render(request, 'logins/register.html')


# from django.contrib.auth.models import User
# from django.shortcuts import render, redirect

# def user_register(request):
#     if request.method == 'POST':
#         email = request.POST.get('username')  # input name is still "username"
#         password = request.POST.get('password')

#         if User.objects.filter(username=email).exists():
#             return render(request, 'logins/register.html', {
#                 'error': 'An account with this email already exists.'
#             })

#         User.objects.create_user(
#             username=email,
#             email=email,
#             password=password
#         )
#         return redirect('home')

#     return render(request, 'logins/register.html')





def user_logout(request):
    logout(request)
    return redirect('login')


def home(request):
    return HttpResponse("This is Home Page")

def success(request):
    return HttpResponse("This is Success Page")