example of django if needing some practice: https://youtu.be/zstmOkteyYI?si=1UFmxYmVT2vpZfu6

How to set up:

1. Install django if not already done so. You can do this on whole computer or a virtual environment. 

2. Make a .env file in main folder (same level as manage.py) and include the following:
    DJANGO_SECRET_KEY = 'key'
    DEBUG='True'

3. Run python3 -c "from django.core.management.utils import get_random_secret_key; print(get_rando
m_secret_key())" in terminal. *it might be python not python3

4. Put that key in your .env file in place of 'key'

5. run python3 migrate. *could be python not python3

Now it is set up hopefully. When you want to test the application you can run python3/python manage.py runserver and go to localhost to see the website. Then run control-c to quit server.
