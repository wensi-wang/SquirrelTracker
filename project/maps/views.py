from .models import sighting
from django.shortcuts import render_to_response, get_object_or_404, redirect

# Create your views here.
def Zone(request):
    Sighting = sighting.objects.all()
    return render_to_response('default.html',{"Sighting":Sighting})
