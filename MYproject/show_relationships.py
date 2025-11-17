import os
import django
from django.conf import settings

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MYproject.settings')
django.setup()

from Myapp.models import Department, Student, Profile, Course

# Create sample data if not exists
dept1 = Department.objects.first() or Department.objects.create(name='Computer Science', description='CS Department')
dept2 = Department.objects.filter(name='Mathematics').first() or Department.objects.create(name='Mathematics', description='Math Department')

# Skip creating new students, just demonstrate relationships with existing data

# Update existing students to have departments
for student in Student.objects.all():
    if not student.department_id:
        student.department = dept1  # Assign to CS department
        student.save()

# Demonstrate relationships
print("=== OneToMany: Department to Students ===")
for dept in Department.objects.all():
    print(f"Department: {dept.name}")
    for student in dept.students.all():
        print(f"  - Student: {student.name}")
    print()

print("=== OneToOne: Student to Profile ===")
for student in Student.objects.all():
    if hasattr(student, 'profile'):
        print(f"Student: {student.name} -> Profile: {student.profile.bio}")
    else:
        print(f"Student: {student.name} -> No Profile")
print()

print("=== ManyToMany: Course to Students ===")
for course in Course.objects.all():
    print(f"Course: {course.name}")
    for student in course.students.all():
        print(f"  - Student: {student.name}")
    print()

print("=== Reverse ManyToMany: Student to Courses ===")
for student in Student.objects.all():
    print(f"Student: {student.name}")
    for course in student.courses.all():
        print(f"  - Course: {course.name}")
    print()
