from django.shortcuts import render,redirect

# Create your views here.
from .models import Coffee
import razorpay

from django.views.decorators.csrf import csrf_exempt
def home(request):
    if request.method=='POST':
        name=request.POST.get('name')
        amount=int(request.POST.get('amount')) * 100
        print(name,amount)
        currency = 'INR'
        razorpay_client=razorpay.Client(auth=('rzp_test_CfJDSKVlk7kJJJ','09Yix0ulmXq0vJvMdSgx1ZQ0'))
        payment = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='1'))
        print(payment)
        coffee=Coffee(name=name,amount=amount,payment_id = payment['id'])
        coffee.save()
        return render(request,'home.html',{'payment': payment})
        
    else:
        return render(request,'home.html')
    

@csrf_exempt

def success_view(request):
    if request.method=='POST':
        a=request.POST
        print(a)
        return render(request,'success.html')
    else:
        return render(request,'success.html')