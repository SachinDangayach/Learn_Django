from  django import forms
from lmx.models import Course, CourseStudentData

class Course1Form(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class  CourseStudentDataForm(forms.ModelForm):
    class Meta:
        model = CourseStudentData
        fields = '__all__'
