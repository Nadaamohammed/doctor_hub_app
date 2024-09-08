from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Patients
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}!')
#             return redirect('login')  # Redirect to login page after successful registration
#         else:
#             # Display the form errors
#             for field in form:
#                 for error in field.errors:
#                     messages.error(request, error)
#             # Display non-field errors
#             for error in form.non_field_errors():
#                 messages.error(request, error)
#     else:
#         form = UserCreationForm()
    
#     return render(request, 'register.html', {'form': form})
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Simple validation checks
        if not username or not email or not password:
            messages.error(request, 'All fields are required.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered.')
        else:
            # Create new user
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Account created successfully.')
            return redirect('login')  # Redirect to the login page after successful registration

    return render(request, 'register.html')


from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')  # Redirect to a home page or another page
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')
from django.contrib.auth.models import User

users = User.objects.all()
def profile(request, id):
    user = User.objects.get(id=id)

    return render(request, 'profile.html', {'user': user})



