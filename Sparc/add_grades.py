#add_grades.py
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Sparc.settings")
django.setup()

from main.models import Performance

def add_grades():
    performances = Performance.objects.all()
    counter = 1

    for performance in performances:
        score = performance.score

        if 70<=score<=100:
            grade = 'A'
        elif 60<=score<=69:
            grade='B'
        elif 50<=score<=59:
            grade='C'
        elif 40<=score<=49:
            grade='D'
        elif 0<=score<=39:
            grade='E'

        performance.grade = grade
        performance.save()
        print(f"{counter}. Updated score for {performance.user.first_name}, {performance.unit.name}: {performance.grade}")
        counter = counter + 1

if __name__ == "__main__":
    add_grades()
