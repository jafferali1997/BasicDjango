import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'AllLecture.settings')

import django
django.setup()

from Lecture.models import UserInfoModel
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        fake_name= fakegen.name().split()
        first_name= fake_name[0]
        last_name= fake_name[1]
        e_mail= fakegen.email()

        user = UserInfoModel.objects.get_or_create(FirstName=first_name,LastName=last_name,Email=e_mail)[0]

if __name__ == '__main__':
    print("POPULATING DATABASE")
    populate(20)
    print("DATABASE POPULATED")