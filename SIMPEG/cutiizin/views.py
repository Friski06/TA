from django.shortcuts import render

def cutiizin(request):
    context = {
        'name' : 'Cuti Izin',
    }
    return render(request,'cutiizin/cutiizin.html',context)