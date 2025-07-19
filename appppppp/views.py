from django.shortcuts import render
from .models import *
def index(request):
    cat = Category.objects.all()

    print(cat)
    context = {
        "cat":cat,
        "title":"Category Title",

    }
    return render(request,'index.html',context=context)
def index1(request):

    con = Country.objects.all()

    print(con)
    context = {

        "con":con,
        "title1":"Country",

    }
    return render(request,'index.html',context=context)
def index2(request):

    wat = Water.objects.all()
    print(wat)
    context = {

        "wat":wat,
        "title2":"Water"
    }
    return render(request,'index.html',context=context)
# Create your views here.








# Create your views here.
