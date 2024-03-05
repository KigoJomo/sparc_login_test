#update_sessions.py
import os
import django
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Sparc.settings")
django.setup()

from main.models import Session

def update_sessions():
    sessions = Session.objects.filter(session_duration_mins=20)

    for session in sessions:
        # Update the goal to a random number between 1 and 5
        session.session_duration_mins = random.randint(5, 25)
        print("Updating ...")
        session.save()

if __name__ == "__main__":
    update_sessions()
