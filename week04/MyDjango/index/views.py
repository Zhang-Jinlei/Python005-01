from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponse

from .models import Name


# Create your views here.

def index(request):
    return HttpResponse("Hello Django!")


def year(request, year):
    # return HttpResponse(year)
    return redirect('/2020.html')


def name(request, **kwargs):
    return HttpResponse(kwargs['name'])


def myyear(request, year):
    return render(request, 'yearview.html')


def books(request):
    n = Name.objects.all()
    return render(request, 'bookslist.html', locals())
