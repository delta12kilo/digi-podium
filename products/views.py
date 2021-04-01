from django.shortcuts import render, redirect

# Create your views here.
def testp(request):
    return render(request,'products/test.html')
