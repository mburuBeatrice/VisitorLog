from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Q
from .models import Visitor
from .forms import VisitorForm
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


