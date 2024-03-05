# add_sessions.py
import os
import django
from datetime import datetime, timedelta

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Sparc.settings")
django.setup()

from main.models import CustomUser, Session

def add_sessions_to_database():
    users = CustomUser.objects.all()

    for user in users:
        daily_goal_hours = user.daily_goal
        focus_period_minutes = user.focus_period
        break_duration_minutes = user.break_duration

        # Calculate the total session duration in minutes for the daily goal
        total_daily_goal_minutes = daily_goal_hours * 60

        # Calculate the number of sessions needed to meet the daily goal
        number_of_sessions = total_daily_goal_minutes / (focus_period_minutes + break_duration_minutes)

        # Set the start date to a week ago
        start_date = datetime.now().date() - timedelta(days=7)

        # Create sessions for each day in the past week
        for _ in range(7):
            # Create sessions to meet the daily goal
            for _ in range(int(number_of_sessions)):
                Session.objects.create(
                    user=user,
                    session_duration_mins=focus_period_minutes,
                    session_duration_sec=0,
                    date=start_date,
                    goal=daily_goal_hours
                )

                Session.objects.create(
                    user=user,
                    session_duration_mins=break_duration_minutes,
                    session_duration_sec=0,
                    date=start_date,
                    goal=0
                )

            # Move to the next day
            start_date += timedelta(days=1)

if __name__ == "__main__":
    add_sessions_to_database()
