from django import forms
from myapp1.models import Course,Teacher

class ModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['c_name','c_photo','fee','c_note']