from django.shortcuts import render,redirect
from .forms import ContactForms


def HomeView(request):
    if request.POST:
        form = ContactForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
        
    form = ContactForms()
    
    ctx = {
        'forms':form
    }
    
    return render(request,'index.html',ctx)
    
