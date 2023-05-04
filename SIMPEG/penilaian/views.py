from django.shortcuts import render

# Create your views here.

def penilaian(request):
    context = {
        'name' : 'Penilaian',
    }
    return render(request,'penilaian/penilaian.html', context)