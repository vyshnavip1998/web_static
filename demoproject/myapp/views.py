from django.shortcuts import render
from django.http import HttpResponse

from .models import Place
from .models import Meet


def demo(request):
    obj = Place.objects.all()
    obj2 = Meet.objects.all()
    return render(request, "index.html", {'result': obj, 'result2': obj2})
