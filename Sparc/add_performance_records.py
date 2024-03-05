#add_performance_records.py
import os
import django
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Sparc.settings")
django.setup()

from main.models import CustomUser, Unit, Performance

def add_performances():
    users = CustomUser.objects.all()
    for user in users:
        units = Unit.objects.filter(course=user.course)
        for unit in units:
            if unit.year <= user.year:
                if unit.semester <= user.semester:
                    score = random.randint(10, 99)
                    Performance.objects.create(user=user, unit=unit, score=score)
                    print(f"Performance created - User: {user.email}, Unit: {unit.code}, Score: {score}")

if __name__ == '__main__':
    print('Adding performance records...')
    add_performances()
    print('Done adding performance records!')
