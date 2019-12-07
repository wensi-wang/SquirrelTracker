from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
from squirreldata.models import sighting
import os
import csv
import re

class Command(BaseCommand):
    help = "Import 'Model'.csv into 'Model' database."
    def add_arguments(self,parser):
        parser.add_argument('csv_file',nargs='+',type=str)

    def handle(self, *args, **options):
        for csv_file in options['csv_file']:
            dataReader = csv.reader(open(csv_file),delimiter=',',quotechar='"')
            next(dataReader, None)
            for row in dataReader:
                #print(row)
                sqr=sighting()
                sqr.longitude=row[0]
                sqr.latitude=row[1]
                sqr.unique_squirrel_id=row[2]
                sqr.shift=row[4]
                sqr.date=row[5]
                sqr.age=row[7]
                sqr.primary_fur_color=row[8]
                sqr.location=row[12]
                sqr.specific_location=row[14]

                #print(row[15])
                if row[15].lower()=='true':
                    sqr.running=True
                elif row[15].lower()=='false':
                    sqr.running=False
                else:
                    sqr.running='running'

                #print(row[16])
                if row[16].lower()=='true':
                    sqr.chasing=True
                elif row[16].lower()=='false':
                    sqr.chasing=False
                else:
                    sqr.chasing='x'

                #print(row[17])
                if row[17].lower()=='true':
                    sqr.climbing=True
                elif row[17].lower()=='false':
                    sqr.climbing=False
                else:
                    sqr.climbing='x'

                #print(row[18])
                if row[18].lower()=='true':
                    sqr.eating=True
                elif row[18].lower()=='false':
                    sqr.eating=False
                else:
                    sqr.eating='x'

                #print(row[19])
                if row[19].lower()=='true':
                    sqr.foraging=True
                elif row[19].lower()=='false':
                    sqr.foraging=False
                else:
                    sqr.foraging='x'

                sqr.other_activities=row[20]

                #print(row[21])
                if row[21].lower()=='true':
                    sqr.kuks=True
                elif row[21].lower()=='false':
                    sqr.kuks=False
                else:
                    sqr.kuks='x'

                #print(row[22])
                if row[22].lower()=='true':
                    sqr.quaas=True
                elif row[22].lower()=='false':
                    sqr.quaas=False
                else:
                    sqr.quaas='x'

                #print(row[23])
                if row[23].lower()=='true':
                    sqr.moans=True
                elif row[23].lower()=='false':
                    sqr.moans=False
                else:
                    sqr.moans='x'

                #print(row[24])
                if row[24].lower()=='true':
                    sqr.tail_flags=True
                elif row[24].lower()=='false':
                    sqr.tail_flags=False
                else:
                    sqr.tail_flags='x'

                #print(row[25])
                if row[25].lower()=='true':
                    sqr.tail_twitches=True
                elif row[25].lower()=='false':
                    sqr.tail_twitches=False
                else:
                    sqr.tail_twitches='x'

                #print(row[26])
                if row[26].lower()=='true':
                    sqr.approaches=True
                elif row[26].lower()=='false':
                    sqr.approaches=False
                else:
                    sqr.approaches='x'

                #print(row[27])
                if row[27].lower()=='true':
                    sqr.indifferent=True
                elif row[27].lower()=='false':
                    sqr.indifferent=False
                else:
                    sqr.indifferent='x'

                #print(row[28])
                if row[28].lower()=='true':
                    sqr.runs_from=True
                elif row[28].lower()=='false':
                    sqr.runs_from=False
                else:
                    sqr.runs_from='x' 

                sqr.save()

