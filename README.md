# BreadBox: Your Personal Bread Recipe Companion

## Description
"BreadBox" is your personal bread recipe companion, accessible through your local host. With this app, you can create a private collection of your favorite bread recipes and enhance your bread-baking journey. You'll have the ability to register and log in to your account securely. Once logged in, you can explore a variety of bread recipes, each presented with detailed instructions and ingredient lists.

The app allows you to save recipes that pique your interest to your personal collection, so you can easily access them whenever you're ready to bake.

After trying a recipe, you can add personal notes to document your baking experiences, such as modifications you made, the outcome of your bake, or any tips and tricks you've discovered. These notes are entirely private and won't be shared with anyone else.

The app aims to make your bread-baking process more enjoyable and organized by providing you with a personalized space to curate your own bread recipe collection and track your unique baking journey.

## Key Features
- **Recipe Collection**: Create and maintain a personal collection of your favorite bread recipes through the admin interface.
- **Secure User Accounts**: Register and log in securely to manage your recipes and notes.
- **Save Favorite Recipes**: Save recipes of interest to your personal collection for easy access.
- **Personalized Notes**: Document your baking experiences with personal notes, such as modifications, outcomes, and tips.
- **Privacy and Security**: Your notes are entirely private and won't be shared with anyone else.


## Running the App
To run the "BreadBox" app locally, follow these steps:

1. **Prerequisites:**
   - Make sure you have Python 3.x and Django installed on your system.

2. **Clone the Repository:**
   ```bash
   git clone https://github.com/alyssawalter/breadbox.git
   cd breadbox
```
   
3. Set Up a Virtual Environment (Optional):
   - It's a good practice to use a virtual environment for your project to isolate dependencies.
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

4. Install Dependencies:
    Install the required Python packages.
   ```bash
   pip install -r requirements.txt
```

5. Migrate the Database:
    Create the database schema and apply migrations.
  ```bash
  python manage.py migrate
```

6. Create a Superuser:
    Create an admin user to access the Django admin interface.
  ```bash
  python manage.py createsuperuser
```

7. Run the Development Server:
    Start the development server.
  ```bash
  python manage.py runserver
```

8. Access the Application:
    Open a web browser and go to http://127.0.0.1:8000/blog/recipes to access the "BreadBox" app.

9. Access the Admin Interface:
    To access the admin interface, go to http://127.0.0.1:8000/admin/ and log in with the superuser credentials.


Enjoy your bread-baking journey with "BreadBox"!
