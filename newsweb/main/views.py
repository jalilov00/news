from django.shortcuts import redirect, render
from . models import New
from .forms import Forma
# Create your views here.
def index(request):
    a = New.objects.order_by('-id')
    return render(request, 'index.html', {'asa':a})

def form(request):

    a = Forma()
    if request.method == "POST":
        f = Forma(request.POST, request.FILES)
        if f.is_valid():
            f.save()
            return redirect('index')

    return render(request, 'formla.html', {'formalar':a})
def update(request,id):
    new = New.objects.get(id=id)
    form = Forma(instance=new)
    print(request.method)
    if request.method=="POST":
        form = Forma(request.POST,request.FILES,instance=new)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'update.html',{"form":form})

def delete(request, id):
    new = New.objects.get(id=id)
    new.delete()
    return redirect('index')