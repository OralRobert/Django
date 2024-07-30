from django.shortcuts import render,redirect
from .models import addexpense,addexpenseform
from django.contrib.auth.models import User
# Create your views here.

def add_expense(request):
     uid=request.session.get('uid')
     if request.method=='POST':
        #f=addincomeform(request.POST)
        expense=request.POST.get('expense')
        expense_type=request.POST.get('expense_type')
        expense_date=request.POST.get('expense_date')
        description=request.POST.get('description')
        exp=addexpense()
        exp.expense=expense
        exp.expense_type=expense_type
        exp.expense_date=expense_date
        exp.description=description
        exp.User=User.objects.get(id=uid)
        exp.save()
        return redirect('/')
     else:
        f=addexpenseform
        context={'form':f}
        return render(request,'addexpense.html',context)

    
def expense_list(request):
    #uid=request.session.get('uid')
    #elist=addexpense.objects.filter(User=uid)
    #elist=addexpense.objects.all()
    #context={'elist':elist}
    #return render(request,'expenselist.html',context)

    uid=request.session.get('uid')
    elist=addexpense.objects.filter(User=uid)
    #elist=addexpense.objects.all()
    elistype=set()
    for i in elist:
        elistype.add(i.expense_type)
    context={'elist':elist,'elistype':elistype}
    return render(request,'expenselist.html',context)

def delete_expenselist(request,elid):
    enc=addexpense.objects.get(id=elid)
    enc.delete()
    return redirect('/expenselist')

def exp_search(request):
    uid=request.session.get('uid')
    srch=request.POST.get('srch')
    elist=addexpense.objects.filter(User=uid,description__contains=srch)
    context={'elist':elist}
    return render(request,'expenselist.html',context)

def sort_by_type(request,ext2):
    uid=request.session.get('uid')
    elist=addexpense.objects.filter(User=uid)
    elistype=set()
    for i in elist:
        elistype.add(i.expense_type)
        elist=addexpense.objects.filter(User=uid,expense_type=ext2)
    context={'elist':elist,'elistype':elistype}
    return render(request,'expenselist.html',context)