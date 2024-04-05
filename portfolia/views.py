from django.shortcuts import render
from .forms import ContactForms


def HomeView(request):
    if request.POST:
        form = ContactForms(request.POST)
        if form.is_valid():
            form.save()
        
    form = ContactForms()
    
    ctx = {
        'forms':form
    }
    
    return render(request,'index.html',ctx)
    
