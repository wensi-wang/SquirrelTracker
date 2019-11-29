from django.shortcuts import render

from django.http import HttpResponse 

from .models import sighting

def all_squirrels(request):
    squirrels = sighting.objects.all()
    context = {
        'squirrels': squirrels,
    }
    return render(request, 'squirreldata/all.html', context)

def update_sighting_info(request,



def create_new_sighting


def delete_sighting
