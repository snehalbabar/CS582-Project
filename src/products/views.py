from django.shortcuts import render, get_object_or_404
from .forms import ProductForm, RawProductForm
from .models import product

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
    obj = product.objects.get(id=my_id)
    # context = {
    #     "title" :obj.title,
    #     "desc" : obj.decs,
    #     "price" :  obj.price        
    # }
    context = {
        'object' : obj
    }
    return render(request,"product/detail.html", context)

