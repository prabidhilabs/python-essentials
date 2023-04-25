####Heading

-First of all i created the folder named watchmateapi inside the home folder
-I opened that folder in the terminal

-Then i created virtual environment by opening inside the terminal using the following command
--> python -m venv menv
-->source menv/bin/activate #which help to activate the virtual environment

-Then i installed the django inside the virtual environment using the following command in terminal
--> pip install django
-->python -m pip install --upgrade pip #for upgrade the pip
-->pip install djangorestframework

-To see the dependencies inside the virtual environment use this command
-->pip freeze

-After that i opened the folder in vs code and inside the virtual environment in vs code terminal

-Used following command start project
-->jdango-admin startproject watchmate

-Then to keep the menv inside storage ran the below command
-->cd watchlist

-Then for start the app i used the below command inside the venv virtual environment

--> python manage.py startapp watchlist

-Then for the migration process inside the menv i ran the below command
-->python manage.py makemigrations

-->python manage.py migrate

-For the creation of super user i ran the below command

--> python manage.py createsuperuser

    name: any
    email: any@gmail.com
    pw: **\*\***

-Then ran server using the following command in terminal
--> python manage.py runserver

-The opened the link 127.0.0.1:8000 in browser

-after that we can do front end side this browser and to open the admin panel we have to search the
-127.0.0.1:8000/admin/

-To work in the rest_framework used the below command
-->pip install djangorestframework

--to work for the restframework i deleted the url.py folder from the watchlist
--i also commented the all code inside the views.py file of watchlist
--the i created the api folder inside the watchlist

--i connected between the main urls.py and watchlist's urls.py file

-- to show the data in jsonresponse we have to search in search bar using /movie/list/ which shows every data in json format

-- but to see the data in through the keywise we have to search using the /movie/1/ , /movie/2/ etc which shows data of first key of 1 second key of secon and so on
