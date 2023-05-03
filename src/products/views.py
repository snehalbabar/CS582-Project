from django.shortcuts import render

from .models import product

# Create your views here.
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
