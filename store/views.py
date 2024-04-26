from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator


def category_summary(request):
    categories = Category.objects.all()
    return render(request, 'layout/category_summary.html', {"categories": categories})


def product(request, pk):
    product: Product = Product.objects.get(id=pk)
    return render(request, 'layout/product.html', {'product': product})


def category(request, foo):
    foo = foo.replace('-', ' ')
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        paginator = Paginator(products, 8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'layout/category.html', {'products': page_obj, 'category': category})
    except:
        messages.success(request, "That Category Doesn't Exist...")
        return redirect('home')


def home(request):
    products = Product.objects.all()
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'layout/home.html', {'products': page_obj})


def about(request):
    return render(request, 'layout/about.html', {})


def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already taken')
            return redirect('signup')
        if password != password_confirm:
            messages.error(request, 'Passwords don\'t match')
            return redirect('signup')

        User.objects.create(
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
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.get(username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid Password or Username')
            return redirect('login')

    return render(request, 'authentication/login.html')


def user_logout(request):
    logout(request)
    return redirect('home')


def navbar(request):
    user_id = request.session.get('user_id')
    return render(request, 'layout/navbar.html', {"user_id": user_id})
