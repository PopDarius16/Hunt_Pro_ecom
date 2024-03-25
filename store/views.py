from .models import Product
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model  # Import the get_user_model function
# Create your views here.


def product(request,pk):
    product: Product = Product.objects.get(id=pk)
    return render(request, 'layout/product.html', {'product' : product})


def home(request):
    products = Product.objects.all()
    return render(request, 'layout/home.html', {'products': products})


def about(request):
    return render(request, 'layout/about.html', {})


def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already taken')
            return redirect('signup')

        user = User.objects.create(
            email=email,
            username=username,  # Make sure username is set correctly based on your user model
            first_name=first_name,
            last_name=last_name,
            password=password
        )

        messages.success(request, 'Account created successfully. Please log in.')
        return redirect('login')

    return render(request, 'authentication/signup.html')


User = get_user_model()  # Get the user model dynamically


def user_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Use the User model consistently
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'Invalid Email')
            return redirect('login')

        # Correct usage of authenticate function

        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('login')
        else:
            login(request, user)
            return redirect('home')

    return render(request, 'authentication/login.html')


def user_logout(request):
    logout(request)
    return redirect('home')