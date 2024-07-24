from django.shortcuts import render,redirect
from .models import Emp,EmpForm

# Create your views here.

def home(request):
    return render(request,'home.html')

def form(request):
    if request.method=='POST':
        f=EmpForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=EmpForm
        context={'form':f}
        return render(request,'form.html',context)
