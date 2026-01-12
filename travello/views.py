from django.shortcuts import render
from django.http import HttpResponse
#from urllib3 import request
from .models import Destination



""""
def homepage(request):
    dest1=Destination()
    dest1.name="Mumbai"
    dest1.desc="The city that never sleeps"
    dest1.img="destination_1.jpg"
    dest1.price=70000
    dest1.offer=True

    return render(request,'index.html',{'dest':dest1})
    #return HttpResponse('hello')

"""



def homepage(request):
    dests=Destination.objects.all()
    return render(request,'index.html',{'dest':dests}) 

