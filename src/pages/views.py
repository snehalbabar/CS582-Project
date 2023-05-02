from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Welcome To HomePage</h1>")
    return render(request,"home.html",{})

def contact_view(request, *args, **kwargs):
     my_context= {
          "my_text" :"this is contact page",
          "my_number" : 123,
          "my_list" :[123,233,456,332]
     }
     return render(request,"contact.html",my_context)
