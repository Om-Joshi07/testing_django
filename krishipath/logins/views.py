

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
            return redirect('home')     # Works only for existing users; doesn't work for new users
        else:
            return HttpResponse("Invalid Credentials")
        
    return render(request, 'logins/login.html')



def user_register(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip().lower()
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')
        full_name = request.POST.get('full_name', '').strip()

        context = {
            'email_value': email,
            'full_name_value': full_name,
            'error': None
        }

        # Basic empty check for all fields
        if not email or not password or not confirm_password or not full_name:
            context['error'] = 'Please fill in all fields.'
            return render(request, 'logins/register.html', context)

        # Full name validation (at least 2 words with letters only)
        name_parts = full_name.split()
        if len(name_parts) < 2:
            context['error'] = 'Please enter your full name (first and last name).'
            return render(request, 'logins/register.html', context)
        
        if not all(part.isalpha() for part in name_parts):
            context['error'] = 'Name can only contain letters.'
            return render(request, 'logins/register.html', context)

        # Password confirmation check
        if password != confirm_password:
            context['error'] = 'Passwords do not match.'
            return render(request, 'logins/register.html', context)

        # Password strength check (optional)
        if len(password) < 8:
            context['error'] = 'Password must be at least 8 characters long.'
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
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password
            )
            # Add full name to user model (assuming your User model has first_name and last_name)
            name_parts = full_name.split()
            user.first_name = ' '.join(name_parts[:-1])
            user.last_name = name_parts[-1]
            user.save()
            
            return redirect('home')
        
        except Exception as e:
            context['error'] = f'Registration failed. Please try again. Error: {str(e)}'
            return render(request, 'logins/register.html', context)

    return render(request, 'logins/register.html')




def user_logout(request):
    logout(request)
    return redirect('login')


def home(request):
    return HttpResponse("This is Home Page")

def success(request):
    return HttpResponse("This is Success Page")


def home(request):
    return render(request, 'logins/home.html')