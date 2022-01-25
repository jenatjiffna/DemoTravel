from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


# def demo(request):
#     name="india"
#     return render(request,"index1.html",{'obj':name})
# def about(request):
#     return render(request,"about.html")
# def contact(request):
#     return HttpResponse("hai all")

# def input1(request):
#     return render(request,"input1.html")
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     r=x+y
#     return render(request,"addition.html",{'result':r})
from .models import place, pics


def demo(request):
    obj= place.objects.all()
    obj1 = pics.objects.all()
    return render(request,"index.html", {'result' : obj , 'result1':obj1})