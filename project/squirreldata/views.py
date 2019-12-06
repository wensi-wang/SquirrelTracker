from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse 
from django.contrib import messages
from .models import sighting
from .forms import SquirrelForm
from django.db.models import Count


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
    if request.method =='POST':
        obj.delete()
        return redirect("../")
    context = {
        'obj': obj
    }
    return render(request, 'squirreldata/sighting_update.html',context)

def sighting_stats_view(request):
    obj = sighting.objects.all()
    location = sighting.objects.values_list('location',flat=True)
    am = sighting.objects.filter(shift='AM').values_list('shift',flat=True)
    pm = sighting.objects.filter(shift='PM').values_list('shift',flat=True)
    juvenile = sighting.objects.filter(age='Juvenile').values_list('age',flat=True)
    adult = sighting.objects.filter(age='Adult').values_list('age',flat=True)
    gray = sighting.objects.filter(primary_fur_color='Gray').values_list('primary_fur_color',flat=True)
    cinnamon = sighting.objects.filter(primary_fur_color='Cinnamon').values_list('primary_fur_color',flat=True)
    black = sighting.objects.filter(primary_fur_color='Black').values_list('primary_fur_color',flat=True)
    ground_plane = sighting.objects.filter(location='Ground Plane').values_list('location',flat=True)
    above_ground = sighting.objects.filter(location='Above Ground').values_list('location',flat=True)
    tru = sighting.objects.filter(runs_from=True).values_list('runs_from',flat=True) 
    fal = sighting.objects.filter(runs_from=False).values_list('runs_from',flat=True)
    context = {
        'am':am,
        'pm':pm,
        'juvenile':juvenile,
        'adult':adult,
        'gray':gray,
        'cinnamon':cinnamon,
        'black':black,
        'ground_plane':ground_plane,
        'above_ground':above_ground,
        'tru':tru,
        'fal':fal,
        'obj':obj,
        }
    return render(request, 'squirreldata/sighting_stats.html', context)

def maps(request):
    queryset = sighting.objects.all()
    context = {
        'sightings': queryset
        }
    return render(request, 'squirreldata/default.html',context)
    
        
