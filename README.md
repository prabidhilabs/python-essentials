###heading

First of all i created the folder named djangoapi inside the home folder
I opened that folder in the terminal

Then i created virtual environment by opening inside the terminal using the following command
--> python -m venv myenv
-->source myenv/bin/activate #which help to activate the virtual environment

    Then i installed the django inside the virtual environment using the following command in terminal
    --> pip install django
    -->python -m pip install --upgrade pip    #for upgrade the pip

    To see the dependencies inside the virtual environment use this command
    -->pip freeze

After that i opened the folder in vs code and inside the virtual environment in vs code terminal

Used following command start project
-->jdango-admin startproject storage

Then to keep the myenv inside storage ran the below command
-->cd api

Then for start the app i used the below command inside the venv virtual environment

--> python manage.py startapp app

Then for the migration process inside the myenv i ran the below command
-->python manage.py makemigrations

-->python manage.py migrate

For the creation of super user i ran the below command

--> python manage.py createsuperuser

name: any
email: any@gmail.com
pw: **\*\***

Then ran server using the following command in terminal
--> python manage.py runserver

The opened the link 127.0.0.1:8000 in browser
