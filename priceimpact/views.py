from django.shortcuts import render

# Create your views here.
from .forms import mainForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect



def mainview(request):
    if request.method == 'POST':
        form = mainForm(request.POST)
        if form.is_valid():
            symbolname = form.cleaned_data['symbol']
            return redirect('dataview/'+ str(symbolname))

    if request.method == 'GET':
        form = mainForm()
        context = {'form' : form}
        return render(request,'index.html',context=context)


def dataview(request, symbol_id):
    context = {'symbol' : symbol_id}
    return render(request,'dataview.html',context=context)
