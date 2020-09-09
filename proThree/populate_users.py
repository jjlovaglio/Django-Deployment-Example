import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proThree.settings')

import django
django.setup()

import random

from first_app.models import User
from faker import Faker

fakegen = Faker('es_ES')

def populate(N=5):

    for entry in range(N):

        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.email()

        usr = User.objects.get_or_create(
            first_name= fake_first_name,
            last_name= fake_last_name,
            email= fake_email,
        )[0]

if __name__ == "__main__":
    print("populating users!")
    populate(20)
    print("populating complete")

