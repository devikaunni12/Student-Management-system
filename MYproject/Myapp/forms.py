from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'name', 'age', 'dob', 'email', 'phone',
            'address', 'department', 'admission_date', 'photo'
        ]
        widgets = {
            'dob': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
            'admission_date': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
        }
