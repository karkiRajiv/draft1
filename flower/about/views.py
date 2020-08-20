from django.shortcuts import render
from . models import about


def aboutus(request):
    abouts= about.objects.all()

    return render(request,'about.html',{'abouts':abouts},)

