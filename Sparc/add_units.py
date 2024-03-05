# add_units.py
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Sparc.settings")
django.setup()

from main.models import Course, Unit

def add_units_to_database():
    courses_data = [
        {'code': 'C025', 'name': 'BSc Information Technology'},
        {'code': 'E034', 'name': 'BSc Electrical Engineering'},
        {'code': 'C027', 'name': 'BSc Business Information Technology'},
        {'code': 'C028', 'name': 'BSc Computer Science'},
        # Add more courses if necessary
    ]

    for course_data in courses_data:
        course, created = Course.objects.get_or_create(code=course_data['code'], defaults={'name': course_data['name']})
        if created:
            print(f"Added Course: {course}")

        for year in range(1, 5):
            for semester in range(1, 3):
                for unit_number in range(1, 8):
                    unit_code = f"{course.code} {year}{semester}{unit_number:02d}"
                    unit_name = f"Unit {year}{semester}{unit_number}"
                    Unit.objects.create(
                        code=unit_code,
                        name=unit_name,
                        course=course,
                        year=year,
                        semester=semester
                    )
                    print(f"Added Unit: {unit_code}")

if __name__ == "__main__":
    add_units_to_database()
