Step 1: Clone the Repository
Start by cloning the project repository from GitHub:
git clone https://github.com/therealphilix/BlogAPI.git
cd BlogAPI

Step 2: Install the dependencies
Start by installing pipenv
run pip install pipenv
then run pipenv install

Step 3: Make Migrations
run python manage.py makemigrations

Step 4: Run Migrations
run python manage.py migrate

Step 5: Create a Superuser
run python manage.py createsuperuser

Step 6: Start the server
run python manage.py runserver

End Points Include:
http://127.0.0.1:8000/blog/posts/
http://127.0.0.1:8000/blog/authors/
http://127.0.0.1:8000/blog/category/
