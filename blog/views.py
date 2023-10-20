from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Recipe, UserProfile, SavedRecipes, Notes
from .forms import NoteForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return HttpResponse("You're at the blog index!")


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'blog/recipe_list.html', {'recipes': recipes})


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    saved = False
    note_form = NoteForm()

    if request.method == 'POST':
        if 'save_recipe' in request.POST:
            saved_recipe, created = SavedRecipes.objects.get_or_create(user=request.user, recipe=recipe)
            saved = True
        elif 'save_note' in request.POST:
            note_form = NoteForm(request.POST)
            if note_form.is_valid():
                new_note = note_form.save(commit=False)
                new_note.user = request.user
                new_note.recipe = recipe
                new_note.save()

    return render(request, 'blog/recipe_detail.html', {'recipe': recipe, 'saved': saved, 'note_form': note_form})


@login_required
def saved_recipes(request):
    saved_recipes = SavedRecipes.objects.filter(user=request.user)
    return render(request, 'blog/saved_recipes.html', {'saved_recipes': saved_recipes})


@login_required
def recipe_notes(request):
    recipe_notes = Notes.objects.filter(user=request.user)
    return render(request, 'blog/recipe_notes.html', {'recipe_notes': recipe_notes})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            UserProfile.objects.create(user=user)

            # Debugging output
            print(f"User registered: {user.username}")
            
            login(request, user)
            return redirect('recipe_list')
        else:
            # Debugging output for form errors
            print("Form errors:")
            print(form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})


 
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Check if 'next' is in the request POST data
            next_url = request.POST.get('next')

            if next_url:
                return redirect(next_url)
            else:
                return redirect('recipe_list')            
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('recipe_list')  # Redirect to the homepage or another appropriate view


def user_profile(request):
    if request.user.is_authenticated:
        print(request.user)
        user_profile = get_object_or_404(UserProfile, user=request.user)
        # You can add more context data based on user_profile
        return render(request, 'blog/user_profile.html', {'user_profile': user_profile})
    else:
        # Handle the case where the user is not authenticated
        return redirect('user_login')  # Redirect to the login page


