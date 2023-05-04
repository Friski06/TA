from django.shortcuts import render

def dataabsen(request):
    context = {
        'name' : 'Data Absen',
    }
    return render(request,'dataabsen/dataabsen.html',context)