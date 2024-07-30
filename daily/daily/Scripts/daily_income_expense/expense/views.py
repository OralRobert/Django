from django.shortcuts import render,redirect
from .models import Expense,Expenseform
# Create your views here.

from django.contrib.auth.models import User


def add_expense(request):
    uid=request.session.get('uid')
    if request.method=='POST':
        expense=request.POST.get('expense')
        expense_type=request.POST.get('expense_type')
        expense_date=request.POST.get('expense_date')
        description=request.POST.get('description')
        inc=Expense()
        inc.expense=expense
        inc.expense_type=expense_type
        inc.expense_date=expense_date
        inc.description=description
        inc.user=User.objects.get(id=uid)
        inc.save()
        return redirect('/')
    else:
        f=Expenseform
        context={'form':f}
        return render(request,'expense.html',context)

def expense_list(request):
    #uid=request.session.get('uid')
    #elist=addexpense.objects.filter(User=uid)
    #elist=addexpense.objects.all()
    #context={'elist':elist}
    #return render(request,'expenselist.html',context)
    uid=request.session.get('uid')
    exp=Expense.objects.filter(user=uid)
    # exp=Expense.objects.all()
    expt=set()
    for i in exp:
        expt.add(i.expense_type)
    context={'exp':exp,'expt':expt}
    return render(request,'expenselist.html',context)

def exp_search(request):
    uid=request.session.get('uid')
    srch=request.POST.get('srch')
    exp=Expense.objects.filter(user=uid,description__contains=srch)
    context={'exp':exp}
    return render(request,'expenselist.html',context)

def sort_by_type(request,ext2):
    uid=request.session.get('uid')
    exp=Expense.objects.filter(user=uid)
    expt=set()
    for i in exp:
        expt.add(i.expense_type)
        exp=Expense.objects.filter(user=uid,expense_type=ext2)
    context={'exp':exp,'expt':expt}
    return render(request,'expenselist.html',context)





