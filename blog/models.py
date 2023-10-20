from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    saved_recipes = models.ManyToManyField('Recipe', related_name='saved_by', blank=True)


    def __str__(self):
        return self.user.username  # Display the username as the user's string representation


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='recipe_images/', blank=True, null=True)
    ingredients = models.TextField()
    instructions = models.TextField()

    servings = models.PositiveIntegerField(null=True, blank=True)
    prep_time = models.PositiveIntegerField(null=True, blank=True)
    cook_time = models.PositiveIntegerField(null=True, blank=True)
    rise_time = models.PositiveIntegerField(null=True, blank=True)
    total_time = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.title


class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    note_content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self): 
        return f"Note for {self.recipe.title} by {self.user.user.username}"


class SavedRecipes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved_recipes')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s saved recipe: {self.recipe.title}"

