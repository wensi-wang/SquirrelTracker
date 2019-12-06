from django.db import models

from django.db.models import Model

from django.urls import reverse

class sighting(models.Model):
    longitude = models.CharField(
        max_length=17,
        help_text='(Numerical longitude value)',
    )

    latitude = models.CharField(
        max_length=17,
        help_text='(Numerical latitude value)',
    )

    unique_squirrel_id = models.CharField(
        max_length=14,
        help_text="(Identification tag for each squirrel sightings. The tag is comprised of 'Hectare ID' + 'Shift' + 'Date(month+day)' + 'Hectare Squirrel Number'. E.g. 42C-AM-1007-02)",
        unique=True,
    )

    AM = 'Am'
    PM = 'Pm'
    
    SHITF_CHOICES = (
        (AM, 'AM'),
        (PM, 'PM'),
    )
    
    shift = models.CharField(
        max_length=2,
        choices=SHITF_CHOICES,
    )
    
    date = models.CharField(
        max_length=8,
        help_text='(Concatenation of the sighting session month, day and year. E.g. 10142018)',
    )

    JUVENILE = 'Juvenile'
    ADULT = 'Adult'
    
    AGE_CHOICES = (
        (JUVENILE, 'Juvenile'),
        (ADULT, 'Adult'),
    )
    
    age = models.CharField(
        max_length=8,
        choices=AGE_CHOICES,
        null=True,
        blank=True,
    )
    
    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'
    
    PRIMARY_FUR_COLOR_CHOICES = (
        (GRAY, 'Gray'),
        (CINNAMON, 'Cinnamon'),
        (BLACK, 'Black'),
    )
    
    primary_fur_color = models.CharField(
        max_length=8,
        choices=PRIMARY_FUR_COLOR_CHOICES,
        null=True,
        blank=True,
    )
    
    GROUND_PLANE = 'Ground plane'
    ABOVE_GROUND = 'Above ground'
    
    LOCATION_CHOICES = (
        (GROUND_PLANE, 'Ground Plane'),
        (ABOVE_GROUND, 'Above Ground'),
    )
    
    location = models.CharField(
        max_length=12,
        choices=LOCATION_CHOICES,
        null=True,
        blank=True,
    )

    specific_location = models.TextField(
        max_length=255,
        blank=True,
        help_text='(Specific place where squirrel was sighted. E.g. crossing street)',
    )
    
    running = models.BooleanField()
    
    chasing = models.BooleanField()
    
    climbing = models.BooleanField()
    
    eating = models.BooleanField()
    
    foraging = models.BooleanField()
    
    other_activities = models.TextField(
        max_length=255,
        blank=True,
        help_text="(Activities haven't been listed. E.g. digging)",
    )
    
    kuks = models.BooleanField()
    
    quaas = models.BooleanField()
    
    moans = models.BooleanField()
    
    tail_flags = models.BooleanField()
    
    tail_twitches = models.BooleanField()
    
    approaches = models.BooleanField()
    
    indifferent = models.BooleanField()
    
    runs_from = models.BooleanField()

    def get_absolute_url(self):
        return reverse('sighting-detail',kwargs={'id':self.unique_squirrel_id})

