from django.shortcuts import render, redirect
from lmx.models import Course, CourseStudentData
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import  reverse_lazy
from django.core.paginator import Paginator
from lmx.forms import CourseStudentDataForm

# Create your views here.
class CourseListView(ListView):
    model=Course

class CourseCreateView(CreateView):
    model=Course
    success_url=reverse_lazy('index')
    fields=('courseTag','courseName','categoryName','phaseName','sessionCount','total_slots','available_slots')

class CourseUdpateView(UpdateView):
    model=Course
    success_url=reverse_lazy('index')
    fields=('courseTag','courseName','categoryName','phaseName','sessionCount','total_slots','available_slots')

class CourseDeleteView(DeleteView):
    model=Course
    success_url=reverse_lazy('index')

def addData(request,**kwargs):
    form = CourseStudentDataForm()
    course = Course.objects.get(id = kwargs['pk'] )
    if request.method=='POST':
        form = CourseStudentDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'lmx/coursestudentdata_form.html',{'form':form, 'course': course})

def details(request,**kwargs):
    data = CourseStudentData.objects.filter(course_id = kwargs['pk'])
    responseData = []
    for eachEntry in data:
        responseData.append(eachEntry)
    return render(request,'lmx/coursestudentdetails.html',{'data':responseData})



def course_list(request):
    course = Course.objects.all()
    paginator = Paginator(course, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'lmx/course_list.html', {'course_list': page_obj})

def pagination(n):
    end = n*12
    start = end-12
    return start, end

    