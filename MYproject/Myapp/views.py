
from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

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



def dashboard(request):
    # Check if user is logged in
    if request.user.is_authenticated:
        return render(request, "dashboard.html")
    else:
        return redirect("login")

def signup_user(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        pwd = request.POST.get("password")

        if User.objects.filter(username=uname).exists():
            return HttpResponse("Username already exists")

        User.objects.create_user(username=uname, password=pwd)
        return redirect('login')

    return render(request, "signup.html")




def login_user(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        pwd = request.POST.get("password")

        user = authenticate(request, username=uname, password=pwd)

        if user:
            login(request, user)          # Session created automatically
            return redirect("index")
        else:
            return HttpResponse("Invalid username or password")

    return render(request, "login.html")




def logout_user(request):
    logout(request)    # session destroyed

    return HttpResponse("Logged out successfully!")








   

   