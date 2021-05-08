from django.shortcuts import render, get_object_or_404, redirect
from .models import About, Payment
from .forms import PaymentForm
from django.urls import reverse
# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    ab = About.objects.all()
    return render(request,'digi/home.html',{'ab':ab})

def testform(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            # print(form.data)
            # return redirect(reverse('post',kwargs={'post':post}))
            return redirect('/test')

    else:       
        form = PaymentForm()
    return render(request, 'digi/register.html', {'form': form})

def post(request, pay_id):
        
        payy = Payment.objects.filter(pay_id = pay_id)
        
        return render(request,'digi/conf_paymnt.html',{
                'payy':payy
            })