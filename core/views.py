from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def indexview(request):
    examlist = Exam.objects.all()
    timetable_list = TimeTable.objects.all().order_by('-updated')

    query = request.POST.get('exam')
    if query:
        examlist = Exam.objects.filter(exam_pin=query)
        # examlist = get_object_or_404(Exam,exam_pin=query)
        if not examlist.exists():
           messages.error(request,"Invalid pin")
        
    else:
        examlist = Exam.objects.none()
    return render(request,'index.html',{'examlist':examlist,'timetable_list':timetable_list})

@login_required
def adminview(request):
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
        if examform.is_valid():
            new_exam=examform.save(commit=False)
            new_exam.author = request.user
            new_exam.save()
            messages.success(request,'Exam has been Posted')
            return redirect('myadmin')

        else:
            messages.error(request,"Error Uploading Exam")

    return render(request,'myadmin.html',{'examlist':examlist,'examform':examform,'timetable_list':timetable_list,'examfilter':examfilter})

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
