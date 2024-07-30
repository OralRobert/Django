from django.shortcuts import render,redirect
from .models import addincome,addincomeform
from django.contrib.auth.models import User
# Create your views here.

def add_income(request):
    uid=request.session.get('uid')
    if request.method=='POST':
        #f=addincomeform(request.POST)
        income=request.POST.get('income')
        income_type=request.POST.get('income_type')
        income_date=request.POST.get('income_date')
        description=request.POST.get('description')
        inc=addincome()
        inc.income=income
        inc.income_type=income_type
        inc.income_date=income_date
        inc.description=description
        inc.User=User.objects.get(id=uid)
        inc.save()
        return redirect('/')
    else:
        f=addincomeform
        context={'form':f}
        return render(request,'addincome.html',context)
    

def income_list(request):
    uid=request.session.get('uid')
    ilist=addincome.objects.filter(User=uid)
   # ilist=addincome.objects.all()
    context={'ilist':ilist}
    return render(request,'incomelist.html',context)

def delete_incomelist(request,ilid):
    inc=addincome.objects.get(id=ilid)
    inc.delete()
    return redirect('/incomelist')

def inc_search(request):
    uid=request.session.get('uid')
    srch=request.POST.get('srch')
    ilist=addincome.objects.filter(User=uid,description__contains=srch)
    context={'ilist':ilist}
    return render(request,'incomelist.html',context)

