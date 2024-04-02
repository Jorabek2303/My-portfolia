from django.shortcuts import render
from .models import ContactModel
from .forms import ContactForms


def HomeView(request):
    
    
    return render(request,'index.html',{})
    
