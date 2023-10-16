from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Recipe, UserProfile
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

def index(request):
    return HttpResponse("You're at the blog index!")


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'blog/recipe_list.html', {'recipes': recipes})


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'blog/recipe_detail.html', {'recipe': recipe})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_profile')  # Redirect to the user's profile page
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('user_profile')  # Redirect to the user's profile page
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('homepage')  # Redirect to the homepage or another appropriate view



def user_profile(request):
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        # You can add more context data based on user_profile
        return render(request, 'blog/user_profile.html', {'user_profile': user_profile})
    else:
        # Handle the case where the user is not authenticated
        return redirect('user_login')  # Redirect to the login page


