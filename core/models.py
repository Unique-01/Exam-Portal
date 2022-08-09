from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.urls import reverse
import datetime

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

    def older_than_a_day(self):
        return (datetime.date.today() - self.date_posted.date()).days > 3
    # def get_absolute_url(self):
    #     return reverse('examdetailsitemap', args=[str(self.id)])



class TimeTable(models.Model):
    title = models.CharField(max_length=500)
    content = RichTextUploadingField()
    date_posted = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(max_length=10,choices=STATUS,default='loading')

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('timetable', args=[str(self.id)])







