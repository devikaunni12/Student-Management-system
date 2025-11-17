from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    dob = models.DateField(verbose_name="Date of Birth")
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='students')
    photo = models.ImageField(upload_to='student_photos/', blank=True, null=True)
    admission_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    hobbies = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.student.name}"


class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True, null=True)
    students = models.ManyToManyField(Student, related_name='courses')

    def __str__(self):
        return self.name
