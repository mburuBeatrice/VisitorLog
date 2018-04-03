from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Q
from .models import Visitor
from .forms import VisitorForm

# Create your views here.
def index(request):
    mgeni_list = Visitor.objects.all()
    page = request.GET.get('page', 1)

    query = request.GET.get("q")
    if query:
        mgeni_list = mgeni_list.filter(
            Q(name__icontains=query) |
            Q(id__icontains=query)
            ).distinct()

    paginator = Paginator(mgeni_list, 1)
    try:
        mgeni = paginator.page(page)
    except PageNotAnInteger:
        mgeni = paginator.page(1)
    except EmptyPage:
        mgeni = paginator.page(paginator.num_pages)
    context ={
        "mgeni": mgeni 
    }
    return render(request, 'index.html', context)


def detail(request, id):

    instance = get_object_or_404(Visitor,id=id)
    

    context = {
    "name":instance.name,
    "instance" : instance
    }
    return render(request, 'visitor_detail.html', context)

def create(request):
    form = VisitorForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,"Successfully created a visitor")
        return HttpResponseRedirect(instance.get_absolute_url())

    else:
        messages.error(request, "Not created")

    context = {
        "form" : form,
    }

    return render(request, 'visitor_form.html', context)
    
def update(request, id=None):
    instance = get_object_or_404(Visitor, id=id)
    form = VisitorForm(request.POST or None, instance=instance)
       
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,"Successfully updated a visitor")
        return HttpResponseRedirect(instance.get_absolute_url())

    else:
        messages.error(request, "Not updated")

    context = {
        "name":instance.name,
        "instance":instance,
        "form" : form,
    }

    return render(request, 'visitor_form.html', context)

def delete(request, id=None):
    instance = get_object_or_404(Visitor, id=id)
    instance.delete()
    messages.success(request, "Visitor Deleted")
    return render(request, 'index.html')


