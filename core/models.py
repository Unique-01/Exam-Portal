from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

STATUS = [
    ('LOADING...','loading'),
    ('UPDATED','updated')
]

# Create your models here.
class Exam(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    subject = models.CharField(max_length=500)
    exam_pin = models.PositiveIntegerField(unique=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    content = RichTextUploadingField(null=True)
    exam_type = models.CharField(max_length=200)
    status = models.CharField(max_length=10,choices=STATUS,default='loading')

    def __str__(self):
        return self.subject



class TimeTable(models.Model):
    title = models.CharField(max_length=500)
    content = RichTextUploadingField()
    date_posted = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(max_length=10,choices=STATUS,default='loading')

    def __str__(self):
        return self.title




    


