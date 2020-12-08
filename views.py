from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Item

def index(request):
    val=Item.objects.all()
    return render(request,'todo/index.html',{
        "all_items":val,
    })
    
def addTodo(request):
    new_item=Item(comment=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')

def delTodo(request, del_id):
    item_del=Item.objects.get(pk=del_id)
    item_del.delete()
    return HttpResponseRedirect("/todo/")
    