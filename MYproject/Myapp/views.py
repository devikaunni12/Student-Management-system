
from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_students')  # redirect after saving
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

def datas(request):
    return render(request, 'data.html')


def view_students(request):
    students =  Student.objects.all()  # fetch all student records
    return render(request, 'view_students.html', {'students': students})


def delete_student(request, pk):
    s= Student.objects.filter(pk=pk).first() 
    if s:
        s.delete()
        s = Student.objects.all()
    return render(request,'view_students.html',{'students':s})


def edit(request, id):
    s = Student.objects.get(pk=id)

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=s)
        if form.is_valid():
            form.save()
            return redirect('view_students')
    else:
        form = StudentForm(instance=s)

    return render(request, 'update.html', {'myform': form})



   