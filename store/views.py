import googlemaps
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from Hunt_Pro_ecom import settings
from .models import Product, Category, Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateUserForm, ChangePasswordForm, UserInfoForm

from payment.forms import ShippingForm
from payment.models import ShippingAddress

from django import forms
from django.db.models import Q
import json
from cart.cart import Cart


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        searched = Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))
        if not searched:
            messages.success(request, "Produsul respectiv nu există... Vă rugăm să încercați din nou!")
            return render(request, "layout/search.html", {})
        else:
            return render(request, "layout/search.html", {'searched': searched})
    else:
        return render(request, "layout/search.html", {})


def update_info(request):
    if request.user.is_authenticated:
        current_user = Profile.objects.get(user__id=request.user.id)
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)

        form = UserInfoForm(request.POST or None, instance=current_user)
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        if form.is_valid() or shipping_form.is_valid():
            form.save()
            shipping_form.save()

            messages.success(request, "Informațiile tale au fost actualizate.")
            return redirect('home')
        return render(request, "layout/update_info.html", {'form': form,
                                                           'shipping_form': shipping_form})
    else:
        messages.success(request, "Trebuie să fii autentificat pentru a accesa pagina respectivă.")
        return redirect('home')


def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == 'POST':
            form = ChangePasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Parola ta a fost actualizată.")
                login(request, current_user)
                return redirect('update_user')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                    return redirect('update_password')
        else:
            form = ChangePasswordForm(current_user)
            return render(request, "layout/update_password.html", {'form': form})
    else:
        messages.success(request, "Trebuie să fii conectat pentru a vedea pagina respectivă.")
        return redirect('home')


def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)

        if user_form.is_valid():
            user_form.save()

            login(request, current_user)
            messages.success(request, "Utilizatorul a fost actualizat!")
            return redirect('home')
        return render(request, "layout/update_user.html", {'user_form': user_form})
    else:
        messages.success(request, "Trebuie să fii autentificat pentru a accesa pagina respectivă!")
        return redirect('home')


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
        messages.success(request, "Categoria respectivă nu există.")
        return redirect('home')


def home(request):
    products = Product.objects.all()
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'layout/home.html', {'products': page_obj})


def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'layout/product.html', {'product': product})


def about(request):
    return render(request, 'layout/about.html', {})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            current_user = Profile.objects.get(user__id=request.user.id)
            saved_cart = current_user.old_cart
            if saved_cart:
                converted_cart = json.loads(saved_cart)
                cart = Cart(request)
                for key, value in converted_cart.items():
                    cart.db_add(product=key, quantity=value)

            messages.success(request, ("Ai fost autentificat!"))
            return redirect('home')
        else:
            messages.success(request, ("A apărut o eroare, te rog sa incerci din nou..."))
            return redirect('login')

    else:
        return render(request, 'authentication/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ("Ați fost deconectat! Îți mulțumim că ai trecut pe aici și te mai asteptăm."))
    return redirect('home')


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Nume de utilizator creat - "
                                       "Vă rugăm să completați informațiile dvs. de utilizator mai jos!"))
            return redirect('update_info')
        else:
            messages.success(request, ("Hopa! A apărut o problemă la înregistrare, vă rugăm să încercați din nou!"))
            return redirect('register')
    else:
        return render(request, 'authentication/register.html', {'form': form})

