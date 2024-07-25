from django.shortcuts import render,redirect
from .models import Income,Incomeform
# Create your views here.

def income(request):
    if request.method=='POST':
        f=Incomeform(request.POST)
        f.save()
        return redirect('/')
    else:
        f=Incomeform
        context={'form':f}
        return render(request,'income.html',context)

def income_list(request):
    incl=Income.objects.all()
    context={'inc1':incl}
    return render(request,'incomelist.html',context)

def delete(request,iid):
    im=Income.objects.get(id=iid)
    im.delete()
    return redirect('/incomelist')

def edit(request,iid):
    im=Income.objects.get(id=iid)
    if request.method=='POST':
        f=Incomeform(request.POST,instance=im)
        f.save()
        return redirect('/')
    else:
        f=Incomeform(instance=im)
        context={'form':f}
        return render(request,'income.html',context)

