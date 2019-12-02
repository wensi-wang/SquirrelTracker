from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse 
from django.contrib import messages
from .models import sighting
from .forms import SquirrelForm


def sighting_list_view(request):
    queryset = sighting.objects.all()
    context = {
        'object_list': queryset
        }
    return render(request, 'squirreldata/sighting_list.html', context)

def sighting_update_view(request,id):
    obj = get_object_or_404(sighting,unique_squirrel_id=id)

    form = SquirrelForm(request.POST or None, instance=obj)
    context = {
        'form': form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request,"You successfully updated the squirrel sighting data")
        context={
            'form':form
        }
        return redirect('./')
    else:
        context={
            'form':form,
            'error':'The squirrel data was not updated successfully. Please enter in the required information'
        }
        return render(request,'squirreldata/sighting_update.html',context)

def sighting_create_view(request):
    form = SquirrelForm()
    if request.method =='POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            form = SquirrelForm()
            return redirect('../')
    context = {
        'form': form
    }
    return render(request, 'squirreldata/sighting_create.html', context)

def sighting_delete_view(request, id):
    obj = get_object_or_404(sighting,unique_squirrel_id=id)
    obj.delete()
    messages.success(request, 'You successfully deleted the squirrel sighting data')
    return redirect('./')
    context = {
        'obj': obj
    }
    return render(request, 'squirreldata/sighting_delete.html',context)

def maps(request):
    queryset = sighting.objects.all()
    context = {
        'sightings': queryset
        }
    return render(request, 'squirreldata/default.html',context)
    
        
