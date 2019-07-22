from django.shortcuts import render
from django.http import HttpResponse
from home.models import Image, Sports
# Create your views here.


def home(request, cat=None):

    sports = Sports.objects.get(name=cat)
    image = Image.objects.filter(name=cat)
    my_dic = {
        'sports': sports,
        'images': list(image)
    }
    print(list(image)[0].name)
    return render(request, "home (3)-1.html", context=my_dic)


def index(request):
    return render(request, "home (3) (1).html")
