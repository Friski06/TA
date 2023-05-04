from django.shortcuts import render

# Create your views here.
def datapegawai(request):
    context = {
        'name':'Data Pegawai',
    }
    return render(request,'datapegawai/datapegawai.html', context)