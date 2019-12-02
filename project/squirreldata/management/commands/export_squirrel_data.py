from django.core.management.base import BaseCommand, CommandError
from squirreldata.models import sighting
import csv
import os

class Command(BaseCommand):
    help = ("Output the specified model as CSV")

    def add_arguments(self,parser):
        parser.add_argument('csv_file',nargs='+',type=str)

    def handle(self, *args, **options):
        model_class = sighting
        meta = model_class._meta
        for csv_file in options['csv_file']:
            with open(csv_file,'w') as csvfile:
                writer = csv.writer(csvfile)
                row = list()
                for field in meta.fields:
                    row.append(str(field.name))    
                writer.writerow(row)        


                for obj in sighting.objects.all():
                    row = list()
                    for field in meta.fields:
                        #print(field.name)
                        #print(getattr(obj, field.name))
                        row.append(str(getattr(obj, field.name)))
                    #print(row)
                    writer.writerow(row)
