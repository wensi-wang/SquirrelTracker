from django import forms
from django.forms import ModelForm
from squirreldata.models import sighting
import datetime

class SquirrelForm(ModelForm):
    class Meta:
        model = sighting
        fields = '__all__'

    def clean_longitude(self,*args,**kwargs):
        longitude = self.cleaned_data.get('longitude')
        if longitude[:5] != '-73.9':
            raise forms.ValidationError("Longitude of any places in Central Park should starts with '-73.9'")
        if len(longitude) != 17:
            raise forms.ValidationError('Length of longitude value should be 17')
        if longitude[5:]<'49193' or longitude[5:]>'81865':
            raise forms.ValidationError('This is not a valid longitude value within the range of Central Park')
        try:
            int(longitude[5:])
            return longitude
        except:
            raise forms.ValidationError('Valid longitude should be a number')
    def clean_latitude(self,*args,**kwargs):
        latitude = self.cleaned_data.get('latitude')
        if latitude[:3] != '40.':
            raise forms.ValidationError("Latitude of any places in Central Park should starts with '40.'")
        if len(latitude) != 16:
            raise forms.ValidationError('Length of latitude value should be 16')
        if latitude[3:]<'764306' or latitude[3:]>'800620':
            raise forms.ValidationError('This is not a valid latitude value within the range of Central Park')
        try:
            int(latitude[3:])
            return latitude
        except:
            raise forms.ValidationError('Valid latitude should be a number')

    def clean_unique_squirrel_id(self,*args,**kwargs):
        unique_squirrel_id = self.cleaned_data.get('unique_squirrel_id')
        if unique_squirrel_id[1] in '0123456789':
            if unique_squirrel_id[:2] > '42':
                raise forms.ValidationError('From north to south, the maximum number of grid is 42, so your left one or two value of hectare should be less than 43')
            if unique_squirrel_id[2] not in 'ABCDEFGHI':
                raise forms.ValidationError("From east to west, only characters between 'A' and 'I' can represent for grid, so your right value of hectare should be characters from A to I")
            if unique_squirrel_id[4:6] not in ['AM','PM']:
                raise forms.ValidationError('Shift value missed')
            try:
                datetime.datetime.strptime(unique_squirrel_id[7:11], '%m%d')
                return unique_squirrel_id
            except:
                raise forms.ValidationError('Date and month value missed')

        if unique_squirrel_id[1] not in '0123456789':
            if unique_squirrel_id[1] not in 'ABCDEFGHI':
                raise forms.ValidationError("From east to west, only characters between 'A' and 'I' can represent for grid, so your right value of hectare should be characters from 'A' to 'I'")
            if unique_squirrel_id[3:5] not in ['AM','PM']:
                raise forms.ValidationError('Shift value missed')
            try:
                datetime.datetime.strptime(unique_squirrel_id[6:10], '%m%d')
                return unique_squirrel_id
            except:
                raise forms.ValidationError('Date and month value missed')
       
    def clean_shift(self,*args,**kwargs):
        shift = self.cleaned_data.get('shift')
        if not shift:
            raise forms.ValidationError('Please enter a valid shift value')
        return shift

    def clean_date(self,*args,**kwargs):
        date = self.cleaned_data.get('date')
        try:
            datetime.datetime.strptime(date, '%m%d%Y')
            return date
        except:
            raise forms.ValidationError('Please enter a valid date')
