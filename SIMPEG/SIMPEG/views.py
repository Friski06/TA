from django.shortcuts import render

def index(request):
    context = {
        'name' : 'SIMPEG',
    }
    return render(request,'index.html',context)