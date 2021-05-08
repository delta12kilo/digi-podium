from django.shortcuts import render, redirect

from .forms import test_form
# Create your views here.

def test_view(request):

    if request.method == 'POST':
        form = test_form(request.POST)

        if form.is_valid():
            # print(form.data)
            redirect('index')
    
    else:
        form = test_form()

    context = {'form':form}

    return render(request, 'digi/test_home.html', context)
