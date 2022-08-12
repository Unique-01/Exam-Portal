from django import forms
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ExamForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Exam
        fields = ['subject','exam_pin','content','exam_type','status']

class TimeTableForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = TimeTable
        fields = ['title','content','status']

class ExamNewsForm(forms.ModelForm):
    contents = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = ExamNews
        fields = ['title','contents','exam_type']
