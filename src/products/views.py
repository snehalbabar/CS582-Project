from django.shortcuts import render,get_object_or_404
from .forms import ProductForm, RawProductForm
from .models import product
from django.http import Http404
# Create your views here.

def product_create_view(request):
    my_form = RawProductForm()
    if request.method == "POST":
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            product.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = { 
        'form': my_form
    }
    return render(request,"product/create.html", context)


#RAW HTML Method
# def product_create_view(request):
#     if request.method == "POST":
#         my_new_title = request.POST.get('title')
#         print(my_new_title)
#     context = { }
#     return render(request,"product/create.html", context)

# def render_inital_data(request):
#     inital_data = {
#         'title':"this is my awsome title",
#     }
#     obj = product.objects.get(id=1)
#     form = RawProductForm(request.POST or None, initial=inital_data, instance=obj)
#     if form.is_valid():
#         form.save() 
#     context = {
#         'form' : form
#     }
#     return render(request,"product/create.html", context)

 


def product_detail_view(request):
    obj = product.objects.get(id=1)
    # context = {
    #     "title" :obj.title,
    #     "desc" : obj.decs,
    #     "price" :  obj.price        
    # }
    context = {
        'object' : obj
    }
    return render(request,"product/detail.html", context)

def dymanic_lookup_view(request,my_id):
    #obj = product.objects.get(id=my_id)
    #obj = get_object_or_404(product,id=my_id)
    try:
        obj = product.objects.get(id=my_id)
    except product.DoesNotExist:
        raise Http404
    context = {
        'object' : obj
    }
    return render(request,"product/detail.html", context)


def product_delete_view(request,my_id):
    obj = get_object_or_404(product,id=my_id)
    #Post Request
    if request.method == "POST":
        #comfirm delete
        obj.delete()
    context = {
        'object' : obj
    }
    return render(request,"product/delete.html", context)


def product_list_view(request):
    queryset = product.objects.all()
    context = {
        "object_list" : queryset
    }
    return render(request,"product/list.html", context)

