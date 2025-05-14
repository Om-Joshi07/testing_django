

from django.shortcuts import render, redirect, HttpResponse
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

import re
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('username')        

        ''' Since built-in django takes email as authentication field, we fed it with username field but there is email 
            and ofc it is working faf. ( lol )    
        '''

        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)      # authenticate the user in the database
        if user:
            login(request, user)
            return redirect('success')     # Works only for existing users; doesn't work for new users
        else:
            return HttpResponse("Invalid Credentials")
        
    return render(request, 'logins/login.html')


# def user_register(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         try:
#             User.objects.create_user(
#                 username=email,
#                 email=email,
#                 password=password
#             )
#             return redirect('success')
#         except IntegrityError:
#             return HttpResponse("User already exists.")
    
#     return render(request, 'logins/register.html')



# def user_register(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')  # Changed from 'username' to 'email' to match your form
#         password = request.POST.get('password')

#         # Validate email format
#         if not email or '@' not in email:
#             return render(request, 'logins/register.html', {
#                 'error': 'Please enter a valid email address.'
#             })

#         # Check if user exists (by both username and email)
#         if User.objects.filter(username=email).exists() or User.objects.filter(email=email).exists():
#             return render(request, 'logins/register.html', {
#                 'error': 'An account with this email already exists.'
#             })

#         # Create user
#         try:
#             user = User.objects.create_user(
#                 username=email,
#                 email=email,
#                 password=password
#             )
            
#             # Optional: Log the user in directly after registration
#             # user = authenticate(request, username=email, password=password)
#             # if user:
#             #     login(request, user)
            
#             return redirect('home')  # Or 'login' if you want them to log in manually
        
#         except Exception as e:
#             return render(request, 'logins/register.html', {
#                 'error': f'Registration failed: {str(e)}'
#             })

#     return render(request, 'logins/register.html')


# def user_register(request):
#     if request.method == 'POST':
#         email = request.POST.get('email', '').strip()
#         password = request.POST.get('password', '')

#         context = {
#             'email_value': email,  # To repopulate the email field
#             'error': None  # Initialize error as None
#         }

#         # Validate email format
#         if not email or '@' not in email:
#             context['error'] = 'Please enter a valid email address.'
#             return render(request, 'logins/register.html', context)

#         # Check if user exists
#         if User.objects.filter(email=email).exists():
#             context['error'] = 'An account with this email already exists.'
#             return render(request, 'logins/register.html', context)

#         # Create user
#         try:
#             User.objects.create_user(
#                 username=email,
#                 email=email,
#                 password=password
#             )
#             return redirect('success')
        
#         except Exception as e:
#             context['error'] = 'Registration failed. Please try again.'
#             return render(request, 'logins/register.html', context)

#     return render(request, 'logins/register.html')



def user_register(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip().lower()
        password = request.POST.get('password', '')

        context = {
            'email_value': email,  # To repopulate the email field
            'error': None
        }

        # Basic empty check
        if not email or not password:
            context['error'] = 'Please fill in all fields.'
            return render(request, 'logins/register.html', context)

        # Comprehensive email validation
        try:
            validate_email(email)  # Django's built-in validator
        except ValidationError:
            context['error'] = 'Please enter a valid email address (e.g., user@example.com).'
            return render(request, 'logins/register.html', context)
            
        # Additional regex pattern check for stricter validation
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            context['error'] = 'Email must be in format: username@domain.com'
            return render(request, 'logins/register.html', context)

        # Check for valid TLD (top-level domain)
        valid_tlds = ['.com', '.org', '.net', '.edu', '.gov', '.io']  # Add more as needed
        if not any(email.endswith(tld) for tld in valid_tlds):
            context['error'] = 'Please use a valid email domain (.com, .org, etc.)'
            return render(request, 'logins/register.html', context)

        # Check if user exists
        if User.objects.filter(email=email).exists():
            context['error'] = 'An account with this email already exists.'
            return render(request, 'logins/register.html', context)

        # Create user
        try:
            User.objects.create_user(
                username=email,
                email=email,
                password=password
            )
            return redirect('success')
        
        except Exception as e:
            context['error'] = 'Registration failed. Please try again.'
            return render(request, 'logins/register.html', context)

    return render(request, 'logins/register.html')




def user_logout(request):
    logout(request)
    return redirect('login')


def home(request):
    return HttpResponse("This is Home Page")

def success(request):
    return HttpResponse("This is Success Page")