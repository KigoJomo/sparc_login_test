# add_tasks.py
import os
import django
import random
from datetime import datetime, timedelta

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Sparc.settings")
django.setup()

from main.models import CustomUser, Unit, Task

def add_tasks_to_database():
    users = CustomUser.objects.all()
    status_options = ["Pending", "In Progress", "Completed"]
    counter = 1

    for user in users:
        units = Unit.objects.filter(course=user.course, year=user.year, semester=user.semester)

        for _ in range(6):  # Create 6 tasks for each user
            unit = random.choice(units)
            due_date = datetime.now() + timedelta(days=random.randint(1, 30))
            status = random.choice(status_options)

            Task.objects.create(
                title=f"Task for {unit.name}",
                user=user,
                description="This is the description for this task",
                unit=unit,
                status=status,
                due_date=due_date
            )
            print(f"{counter}. Added Task for {user.email}")
            counter = counter + 1

if __name__ == "__main__":
    add_tasks_to_database()
