from django.shortcuts import render
from .forms import ItemForm
from django.http import HttpResponse

# Create your views here.
def pageCount(request):
    count = request.session.get('cont',0)
    count = count + 1
    request.session['count'] = count
    return render(request,'sessionApp/count.html',{'count':count})

def index(request):
    request.session.set_expiry(120)
    if request.session['count']:
        del request.session['count']
    return render(request,'sessionApp/index.html')

def addItem(request):
    form = ItemForm()
    if request.method == 'POST':
        name = request.POST['name']
        quantity = request.POST['quantity']
        request.session[name] = quantity
    return render(request,'sessionApp/addItem.html',{'form':form})

def displayCart(request):
    return render(request,'sessionApp/displayItems.html')
