from . import views
from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('myadmin/timetable_delete/<pk>',views.TimeTableDelete.as_view(),name='timetable_delete'),
    path('myadmin/exam_delete/<pk>',views.ExamDelete.as_view(),name="exam_delete"),
    path('myadmin/exam_update/<id>',views.exam_update,name='exam_update'),
    path('myadmin/timetable_update/<id>',views.timetable_update,name='timetable_update'),
    path('myadmin/timetable',views.timetableview,name='timetable_form'),
    path('myadmin/',views.adminview,name='myadmin'),
    path('',views.indexview,name='home'),
   # path('exam/<id>/',views.examview,name="exam"),
    path('timetable/<id>',views.timetable,name='timetable'),
    path('disclaimer/',TemplateView.as_view(template_name="disclaimer.html"),name='disclaimer'),
    path('about/',TemplateView.as_view(template_name="about.html"),name='about'),
    path('contact/',TemplateView.as_view(template_name="contact.html"),name='contact'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
