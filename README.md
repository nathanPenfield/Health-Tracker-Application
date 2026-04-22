
# Health Tracker Application

This application is an All-In-One health and wellness suite, with built in symptom tracking, medication tracking, exercise logging, and other features. 

This project was a CS 275 Semester long class project, which was designed to teach us the ins and outs of real world software engineering. For this, we took an approach consisting of Agile Engineering, which has been adopted majorly throughout software engineering environments. 




## Setup

1. Install Django if you have not done so already.
2. Make a .env file in main folder (same level as manage.py) and include the following: DJANGO_SECRET_KEY = 'key' DEBUG='True'
3. In terminal, run 
```batch
python
django.core.management.utils import get_random_secret_key
print(get_rando m_secret_key())
```
and then replace key in the .env with the generated key.
4. In Terminal, run
```batch
python manage.py makemigrations
```
and
```
python manage.py migrate
```

Now to test, run
```
python manage.py runserver
```

## Authors

- [@nathanPenfield](https://github.com/nathanPenfield) Nathan Penfield
- [@TJHuck](https://github.com/TJHuck) TJ Huck
- [@pm11-ai](https://github.com/pm11-ai) Pacey Mink

