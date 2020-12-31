from django.shortcuts import render

# Create your views here.

def renderTemplate(request):
    myDict = {'name':"Sachin"}
    return render(request,'templatesApp/firstTemplate.html',context=myDict)

def renderEmployee(request):
    myDict = {'id':162437,'name':"Sachin",'age':39,'salary':'INR 5M'}
    return render(request,'templatesApp/employeeTemplate.html',context=myDict)
