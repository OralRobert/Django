from django.shortcuts import render,redirect
from .models import Income,Incomeform
# Create your views here.

from django.contrib.auth.models import User

def add_income(request):
    uid=request.session.get('uid')
    if request.method=='POST':
        income=request.POST.get('income')
        income_type=request.POST.get('income_type')
        income_date=request.POST.get('income_date')
        description=request.POST.get('description')
        inc=Income()
        inc.income=income
        inc.income_type=income_type
        inc.income_date=income_date
        inc.description=description
        inc.user=User.objects.get(id=uid)
        inc.save()
        return redirect('/')
    else:
        f=Incomeform
        context={'form':f}
        return render(request,'income.html',context)

def income_list(request):
    uid=request.session.get('uid')
    # incl=Income.objects.all()
    incl=Income.objects.filter(user=uid)
    context={'incl':incl}
    return render(request,'incomelist.html',context)

def inc_search(request):
    uid=request.session.get('uid')
    srch=request.POST.get('srch')
    incl=Income.objects.filter(user=uid,description__contains=srch)
    context={'incl':incl}
    return render(request,'incomelist.html',context)




