from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.
def indexpage(request):
 category=Category.objects.all()
 return render(request,'index.html',{'category':category})

def productlist(request,myid):
 product=Product.objects.filter(cat_name=myid)
 return render(request,"products.html",{"product":product})
 
def productdetail(request,pid):
 detail=Product.objects.get(id=pid)
 return render(request,"detail.html",{"detail":detail})
