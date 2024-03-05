# add_outline.py
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Sparc.settings")
django.setup()

from main.models import Unit

def add_outline():
    units = Unit.objects.all()
    for unit in units:
        course_outline = """Week 1: Introduction to {unit.name}
                - Overview of {unit.name}
                - Key Concepts in {unit.name}
                - Learning Objectives

            Week 2: In-depth Study of {unit.name}
                - Detailed Exploration of {unit.name} Topics
                - Practical Exercises and Hands-on Activities

            Week 3: Application and Projects
                - Real-world Applications of {unit.name}
                - Group Projects and Individual Assignments

            Week 4: Assessment and Review
                - Evaluation of {unit.name} Understanding
                - Review of Key Concepts

            Week 5: Conclusion
                - Recap of {unit.name}
                - Future Learning Paths and Resources
        """.format(unit=unit)

        unit.outline = course_outline
        unit.save()
        print(f"Added outline to {unit.name}")

if __name__ == "__main__":
    add_outline()
