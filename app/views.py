
from django.shortcuts import render
from time import strftime, localtime
    
def index(request):
    context = {
        "time":[
        strftime("%d-%m-%Y", localtime()),
        strftime("%H:%M:%S %p", localtime()),]
    }
    return render(request,'index.html', context)
