from django.shortcuts import render
from django.contrib import messages as m

# Create your views here.

def home(request):
    return render(request,'home.html')

def msg1_data(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        passw=request.POST.get('passw')
        if(uname=='rajesh' and passw=='123'):
            lmsg='Login Successfully'
            smsg='Username: '+uname+' '+'Password: '+passw
            context={'lmsg':lmsg,'smsg':smsg}
            return render(request,'msg1.html',context)
        else:
            emsg='Login Error'
            smsg='Username: '+uname+' '+'Password: '+passw
            context={'emsg':emsg,'smsg':smsg}
            return render(request,'msg1.html',context)
    else:
        return render(request,'msg1.html')