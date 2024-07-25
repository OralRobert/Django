from django.shortcuts import render,redirect
from .models import Expense,Expenseform
# Create your views here.

def expense(request):
    if request.method=='POST':
        f=Expenseform(request.POST)
        f.save()
        return redirect('/')
    else:
        f=Expenseform
        context={'form':f}
        return render(request,'expense.html',context)

def expense_list(request):
    exp=Expense.objects.all()
    context={'exp1':exp}
    return render(request,'expenselist.html',context)

def delete1(request,eid):
    em=Expense.objects.get(id=eid)
    em.delete()
    return redirect('/expenselist')

def edit1(request,eid):
    em=Expense.objects.get(id=eid)
    if request.method=='POST':
        f=Expenseform(request.POST,instance=em)
        f.save()
        return redirect('/')
    else:
        f=Expenseform(instance=em)
        context={'form':f}
        return render(request,'expense.html',context)



