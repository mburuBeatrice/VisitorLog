from django.shortcuts import render
from .models import Visitor
# Create your views here.
def index(request):
    mgeni = Visitor.objects.all()

    context ={
        "mgeni": mgeni 
    }
    return render(request, 'index.html', context)