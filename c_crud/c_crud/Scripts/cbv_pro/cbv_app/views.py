from django.shortcuts import render
from django.views.generic import FormView,CreateView,ListView,DeleteView,UpdateView

from .models import EmpForm,Emp

# Create your views here.

def home(request):
    return render(request,'home.html')

class EmpRegister(FormView):
    form_class=EmpForm
    template_name='addemp.html'

class addemp(CreateView):
    model=Emp
    fields='__all__'
    success_url='/'

class emp_list(ListView):
    model=Emp
    template_name='elist.html'

class delete1(DeleteView):
    model=Emp
    success_url='/elist'

class delete2(DeleteView):
    template_name ='delete.html'
    model=Emp
    success_url='/elist'

class edit(UpdateView):
    model=Emp
    fields='__all__'
    template_name='update.html'
    success_url='/elist'

    