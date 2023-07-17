from django.shortcuts import render 
from django.db.models import Q 
from django.http import HttpResponse  
from imageshop.models import * 
# Create your views here.
def home(request): 
    images=Image.objects.all()  
    cats=Category.objects.all() 
    data={'images':images,'cats':cats}  
    return render(request,"home.html",data) 

def show_category_page(request,cid):     
    cats=Category.objects.all()  
    catg=Category.objects.get(pk=cid)   
    images=Image.objects.filter(cat=catg)
    data={'images':images,'cats':cats}  
    return render(request,"home.html",data)   



