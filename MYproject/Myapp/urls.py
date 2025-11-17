from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('student/', views.student_form, name='student_form'),
    path('datas/', views.datas, name='datas'),

    path('view_students/', views.view_students, name='view_students'),
    path('delete/<int:pk>', views.delete_student, name='delete_student'),
    path('edit/<int:id>/', views.edit, name='edit'),
]
