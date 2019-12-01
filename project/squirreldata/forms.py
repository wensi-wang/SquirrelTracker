from django.forms import ModelForm

from squirreldata.models import sighting

class SquirrelForm(ModelForm):
    class Meta:
        model = sighting
        fields = '__all__'
