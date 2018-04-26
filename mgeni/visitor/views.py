from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Q
from .models import Visitor,County
from .forms import VisitorForm,CountyForm
from django.views.generic import View
from io import BytesIO
from django.http import HttpResponse
from django.views.generic import View
from mgeni.utils import render_to_pdf 
from django.template.loader import get_template

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
         template = get_template('pdf/invoice.html')
         context = {
             "invoice_id": 123,
             "customer_name": "John Cooper",
             "amount": 1399.99,
             "today": "Today",
         }
         html = template.render(context)
         pdf = render_to_pdf('pdf/invoice.html', context)
         if pdf:
             response = HttpResponse(pdf, content_type='application/pdf')
             filename = "Invoice_%s.pdf" %("12341231")
             content = "inline; filename='%s'" %(filename)
             download = request.GET.get("download")
             if download:
                 content = "attachment; filename='%s'" %(filename)
             response['Content-Disposition'] = content
             return response
         return HttpResponse("Not found")

# def load_available_rooms(request):
#     room_id = request.GET.get('room')
#     rooms = Room.objects.filter(room_id=room_id).order_by('name')
    
#     return render(request, 'room_options.html', {'rooms':rooms} )


def mainpage(request):

    return render(request, 'main.html')

def index(request):
    mgeni_list = Visitor.objects.all()
    page = request.GET.get('page', 4)

    query = request.GET.get("q")
    if query:
        mgeni_list = mgeni_list.filter(
            Q(name__icontains=query) |
            Q(id__icontains=query)
            ).distinct()

    paginator = Paginator(mgeni_list, 4)
    try:
        mgeni = paginator.page(page)
    except PageNotAnInteger:
        mgeni = paginator.page(4)
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

def load_available_rooms(request):
    room_id = request.GET.get('room')
    rooms = Available.objects.filter(room_id=room_id).order_by('occupancy')
    return render(request,'room_options.html',{'rooms':rooms})



def delete(request, id=None):
    instance = get_object_or_404(Visitor, id=id)
    instance.delete()
    messages.success(request, "Visitor Deleted")
    return render(request, 'index.html')


def county_index(request):
    county_list = County.objects.all()
    page = request.GET.get('page', 4)

    query = request.GET.get("q")
    if query:
        county_list = county_list.filter(
            Q(name__icontains=query) |
            Q(code__icontains=query)
            ).distinct()

    paginator = Paginator(county_list,4)
    try:
        county = paginator.page(page)
    except PageNotAnInteger:
        county = paginator.page(1)
    except EmptyPage:
        county = paginator.page(paginator.num_pages)

    context ={
        "county": county 
    }
    return render(request, 'counties.html', context)

def county_detail(request, id):

    inst = get_object_or_404(County,id=id)
    

    context = {
    "name":inst.name,
    "inst" : inst
    }
    return render(request, 'county_detail.html', context)

def county_create(request):
    form = CountyForm(request.POST or None)
    if form.is_valid():
        inst = form.save(commit=False)
        inst.save()
        messages.success(request,"Successfully created a county")
        return HttpResponseRedirect(inst.get_absolute_url())

    else:
        messages.error(request, "Not created")

    context = {
        "form" : form,
    }

    return render(request, 'county_form.html', context)
    
def county_update(request, id=None):
    inst = get_object_or_404(County, id=id)
    form = CountyForm(request.POST or None, inst=inst)
       
    if form.is_valid():
        inst = form.save(commit=False)
        inst.save()
        messages.success(request,"Successfully updated a county")
        return HttpResponseRedirect(inst.get_absolute_url())

    else:
        messages.error(request, "Not updated")

    context = {
        "name":inst.name,
        "inst":inst,
        "form" : form,
    }

    return render(request, 'county_form.html', context)
def county_delete(request, id=None):
    inst = get_object_or_404(County, id=id)
    inst.delete()
    messages.success(request, "County Deleted")
    return render(request, 'counties.html')
def room_index(request):
    room_list = Room.objects.all()
    page = request.GET.get('page', 4)

    query = request.GET.get("q")
    if query:
        room_list = room_list.filter(
            Q(name__icontains=query) |
            Q(code__icontains=query)
            ).distinct()

    paginator = Paginator(county_list,4)
    try:
        county = paginator.page(page)
    except PageNotAnInteger:
        county = paginator.page(1)
    except EmptyPage:
        county = paginator.page(paginator.num_pages)

    context ={
        "county": county 
    }
    return render(request, 'counties.html', context)

def county_detail(request, id):

    inst = get_object_or_404(County,id=id)
    

    context = {
    "name":inst.name,
    "inst" : inst
    }
    return render(request, 'county_detail.html', context)

def county_create(request):
    form = CountyForm(request.POST or None)
    if form.is_valid():
        inst = form.save(commit=False)
        inst.save()
        messages.success(request,"Successfully created a county")
        return HttpResponseRedirect(inst.get_absolute_url())

    else:
        messages.error(request, "Not created")

    context = {
        "form" : form,
    }

    return render(request, 'county_form.html', context)
    
def county_update(request, id=None):
    inst = get_object_or_404(County, id=id)
    form = CountyForm(request.POST or None, inst=inst)
       
    if form.is_valid():
        inst = form.save(commit=False)
        inst.save()
        messages.success(request,"Successfully updated a county")
        return HttpResponseRedirect(inst.get_absolute_url())

    else:
        messages.error(request, "Not updated")

    context = {
        "name":inst.name,
        "inst":inst,
        "form" : form,
    }

    return render(request, 'county_form.html', context)
def county_delete(request, id=None):
    inst = get_object_or_404(County, id=id)
    inst.delete()
    messages.success(request, "County Deleted")
    return render(request, 'counties.html')



