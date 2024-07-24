from django.shortcuts import render,redirect
from .models import Emp,EmpForm,account,accountForm

# Create your views here.

def home(request):
    return render(request,'home.html')

def emp_details(request):
    if request.method== 'POST':
        f=EmpForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=EmpForm
        context = {'form':f}
        return render(request,'emp_details.html',context)

def emp_account(request):
    if request.method=='POST':
        f=accountForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=accountForm
        context= {'form':f}
        return render(request,'emp_account.html',context)

def emp_list(request):
    emp1=Emp.objects.all()
    context={'elist':emp1}
    return render(request,'emp_list.html',context)

def act_list(request):
    act1= account.objects.all()
    context={'alist': act1}
    return render(request,'act_list.html',context)

def delete_1(request):
    eid=request.GET.get('id')
    em=Emp.objects.get(id=eid)
    em.delete()
    return redirect('/emp_list')

def delete_2(request,eid):
    em=Emp.objects.get(id=eid)
    em.delete()
    return redirect('/emp_list')

def delete(request,eid):
    em=account.objects.get(id=eid)
    em.delete()
    return redirect('/act_list')

def edit(request,eid):
    em=Emp.objects.get(id=eid)
    if request.method=='POST':
        f=EmpForm(request.POST,instance=em)
        f.save()
        return redirect('/emp_list')
    else:
        f=EmpForm(instance=em)
        context = {'form':f}
        return render(request,'emp_details.html',context)

def edit_1(request,eid):
    em=account.objects.get(id=eid)
    if request.method=='POST':
        f=accountForm(request.POST,instance=em)
        f.save()
        return redirect('/')
    else:
        f=accountForm(instance=em)
        context= {'form':f}
        return render(request,'emp_account.html',context)

