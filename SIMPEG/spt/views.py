from django.shortcuts import render

# Create your views here.
def spt(request):
    context = {
        'name' : 'SPT',
    }
    return render(request,'spt/spt.html',context)