from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .models import It_allCourses, sophomore, enrool
from django.http import HttpResponse
from products.forms import registerForms
# from enroll.forms import test_form
from django.http import JsonResponse

# Create your views here.

class cardView(View):

    def get(self,request):
        prod = It_allCourses.objects.all()

        context = {"prod":prod}

        return render(request,'products/test.html', context)

class registerStuff(View):

    def get(self, request, proo, *args, **kwargs):

        pro = get_object_or_404(It_allCourses,courseSlug=proo)
        
        form = registerForms()

        context = {'pro':pro,'form':form}

        return render(request,'digi/test_home.html', context)

    def post(self, request, *args, **kwargs):
        
        form = registerForms(request.POST, request.FILES)

        enr = enrool.objects.all()
        data = {}
        if request.method == "POST":

            if request.is_ajax():

                firstname = request.POST.get('firstName')
                lastname = request.POST.get('lastName')
                mail = request.POST.get('email')
                Price = request.POST.get('price')
                program = request.POST.get('program')
                course = request.POST.get('courses')
                clg = request.POST.get('collegess')
                wph = request.POST.get('WphoneNumber')
                ph = request.POST.get('phoneNumber')
                yr = request.POST.get('years')

                enrl = enrool(
                    firstName= firstname,
                    lastName = lastname,
                    courses = course,
                    email = mail,
                    price = Price,
                    program = program,
                    collegess = clg,
                    WphoneNumber = wph,
                    phoneNumber = ph,
                    year = yr
                )
                enrl.save()
                data['status'] = 200
                data['success'] = 'ok'
                return JsonResponse(data)

            
            # data = {}
            # if request.is_ajax():
            #     if form.is_valid():
            #         form.save()
            #         data['status'] = 200
            #         data['success'] = 'ok'
            #         return JsonResponse(data)

            
            # form = registerForms(request.POST)
            # if form.is_valid():
            #     form.save()
            #     return HttpResponse('')

            # else:
            #     return render(request,'digi/test_home.html', {'form':form})

        context = {'form':form, 'enr':enr}

        return render(request,'digi/test_home.html', context)