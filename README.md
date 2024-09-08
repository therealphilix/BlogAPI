Developed a Blog API using Django, Django REST Framework, and Django JWT. The API includes the following features:

User Authentication: Secure login and registration using JWT tokens.
User Authorization: Role-based access control to manage permissions for different user levels.
Post Management: Create, update, delete, and view blog posts.
Commenting System: Users can add comments to blog posts.
Category Management: Posts can be categorized and filtered by category.
Tagging: Posts can be tagged with relevant keywords for better searchability.
Pagination: API responses support pagination for efficient data retrieval.
Search Functionality: Users can search for posts by title, content, or tags.
User Profiles: Users have profiles with their bio, profile picture, and list of posts


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
