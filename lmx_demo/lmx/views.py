from django.shortcuts import render, redirect
from lmx.models import Course, CourseStudentData
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import  reverse_lazy
from django.core.paginator import Paginator
from lmx.forms import CourseStudentDataForm
from django.db.models import Q

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
    # course_number = request.GET.get('search')
    print('pdk',kwargs['pk'])
    data = Course.objects.filter(id = kwargs['pk'])
    responseData = []
    for eachEntry in data:
        responseData.append(eachEntry)
    return render(request,'lmx/coursestudentdetails.html',{'course_list':data})

def student_details(request,**kwargs):
    # course_number = request.GET.get('search')
    print('pdk',kwargs['pk'])
    data = CourseStudentData.objects.filter(course_id = kwargs['pk'])
    responseData = []
    for eachEntry in data:
        responseData.append(eachEntry)
    return render(request,'lmx/coursestudentdetails.html',{'course_list':data})

def course_list(request):
    search_post = request.GET.get('search')
    if search_post:
        course = Course.objects.filter(Q(courseName__icontains=search_post))
    else:
        course = Course.objects.all()
    paginator = Paginator(course, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'lmx/course_list.html', {'course_list': page_obj})

def pagination(n):
    end = n*12
    start = end-12
    return start, end

    