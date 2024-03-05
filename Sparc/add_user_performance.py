#add_user_performance.py
import os
import django
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Sparc.settings")
django.setup()

from main.models import CustomUser, Unit, Performance

def addPerformances():
    user = CustomUser.objects.get(reg_number="C025-01-0822/2022")
    units = Unit.objects.filter(course=user.course)
    for unit in units:
        if unit.year <= user.year:
            if unit.semester <= user.semester:
                score = random.randint(35, 99)
                Performance.objects.create(
                    user = user,
                    unit = unit,
                    score= score
                )
                print(f"Performance record added for {user.first_name}, {unit.name}, {score}")

if __name__ == "__main__":
    addPerformances()
    print("Done adding performance records.")
