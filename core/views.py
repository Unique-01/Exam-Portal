from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import generic

# Create your views here.


def indexview(request):
    examlist = Exam.objects.all()
    timetable_list = TimeTable.objects.all().order_by('-updated')
    pins = Exam.objects.all()
    update = ExamNews.objects.filter(exam_type='frontpage')

    query = request.POST.get('exam')
    if query:
        examlist = Exam.objects.filter(exam_pin=query)
        # examlist = get_object_or_404(Exam,exam_pin=query)
        if not examlist.exists():
           messages.error(request,"Invalid pin")

    else:
        examlist = Exam.objects.none()
    return render(request,'index.html',{'examlist':examlist,'timetable_list':timetable_list,'pins':pins,'update':update})

#def examview(request,id):
    #exam_obj = get_object_or_404( Exam,id=id)

    #return render(request,"exam.html",{"exam_obj":exam_obj})


@login_required
def adminview(request):
    examnews = ExamNews.objects.all()
    examnewsform = ExamNewsForm()
    examlist = Exam.objects.all().order_by('-updated')
    examform = ExamForm()
    timetable_list = TimeTable.objects.all().order_by('-updated')
    new_exam = None
    examfilter = None
    query = request.GET.get('q')
    if query:
        examfilter = Exam.objects.filter(subject__icontains=query).order_by('-updated')
    if request.method == "POST":
        examform = ExamForm(request.POST)
        examnewsform = ExamNewsForm(request.POST)
        
        if examform.is_valid():
            new_exam=examform.save(commit=False)
            new_exam.author = request.user
            new_exam.save()
            messages.success(request,'Exam has been Posted')
            return redirect('myadmin')

        else:
            messages.error(request,"Error Uploading Exam")

        if examnewsform.is_valid():
            examnewsform.save()
            messages.success(request,'News has been posted')
            return redirect('myadmin')

        else:
            messages.error(request,"Error uploading News")

    return render(request,'myadmin.html',{'examlist':examlist,'examform':examform,'timetable_list':timetable_list,'examfilter':examfilter,'examnewsform':examnewsform,'examnews':examnews})

@login_required
def timetableview(request):
    timetableform = TimeTableForm(request.POST)
    new_timetable = None
    if timetableform.is_valid():
        new_timetable = timetableform.save(commit=False)
        new_timetable.author = request.user
        new_timetable.save()
        messages.success(request,'TimeTable has beeen Uploaded')
        return redirect('myadmin')
    return render(request,'timetable_form.html',{'timetableform':timetableform})

@login_required
def exam_update(request,id):
    obj = get_object_or_404(Exam,id=id)
    update_form = ExamForm(request.POST or None,instance=obj)

    if update_form.is_valid():
        obj = update_form.save(commit=False)
        obj.save()

        messages.success(request,"Exam has been Updated")
        return redirect('myadmin')

    return render(request,'exam_update.html',{'update_form':update_form,})


@login_required
def timetable_update(request,id):
    obj = get_object_or_404(TimeTable,id=id)
    update_form = TimeTableForm(request.POST or None,instance=obj)

    if update_form.is_valid():
        obj = update_form.save(commit=False)
        obj.save()

        messages.success(request,"Timeetable has been Updated")
        return redirect('myadmin')

    return render(request,'timetable_update.html',{'update_form':update_form,})

def timetable(request,id):
    timetable_obj = get_object_or_404(TimeTable,id=id)

    return render(request,'timetable.html',{'timetable_obj':timetable_obj})

class ExamDelete(generic.DeleteView):
    model = Exam
    success_url = '/myadmin'
    template_name = 'exam_delete.html'

    def get_success_url(self):
        messages.success(self.request, "Exam has been deleted successfully")
        return reverse("myadmin")

class TimeTableDelete(generic.DeleteView):
    model = TimeTable
    success_url = '/myadmin'
    template_name = 'timetable_delete.html'

    def get_success_url(self):
        messages.success(self.request, "Timetable has been deleted successfully")
        return reverse("myadmin")

@login_required
def exam_news_update(request,id):
    obj = get_object_or_404(ExamNews,id=id)
    update_form = ExamNewsForm(request.POST or None,instance=obj)

    if update_form.is_valid():
        obj = update_form.save(commit=False)
        obj.save()

        messages.success(request,"Exam News has been Updated")
        return redirect('myadmin')

    return render (request,'exam_news_update.html',{'update_form':update_form,})

class ExamNewsDelete(generic.DeleteView):
    model = ExamNews
    success_url = '/myadmin'
    template_name = 'exam_news_delete.html'

    def get_success_url(self):
        messages.success(self.request, "Exam News has been deleted successfully")
        return reverse("myadmin")

def waec_news(request):
    waec = ExamNews.objects.filter(exam_type='waec')

    return render (request,'waec.html',{'waec':waec})

def neco_news(request):
    neco = ExamNews.objects.filter(exam_type='neco')

    return render (request,'neco.html',{'neco':neco})

def jupeb_news(request):
    jupeb = ExamNews.objects.filter(exam_type='jupeb')

    return render (request,'jupeb.html',{'jupeb':jupeb})

def nabteb_news(request):
    nabteb = ExamNews.objects.filter(exam_type='nabteb')

    return render (request,'nabteb.html',{'nabteb':nabteb})
