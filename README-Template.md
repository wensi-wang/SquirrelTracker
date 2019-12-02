# Squirrel Tracker

This is an application used to track all the known squirrels in Central Park. The initial dataset comes from the 2018 Central Park Squirrel Census, and this application allows you to add, update, and delete squirrel data.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Python 3 is strongly recommended for this tutorial because Python 2 will no longer be supported starting January 1, 2020. Python 3.7 to was used to build this tutorial. We will also use the following application dependencies to build our application:
* Django web framework, version 2.2.7
* pip and virtualenv, which come installed with Python 3, to install and isolate the Django library from your other applications
```

## Runing this Application

These instructions will decribe the use and behavior of our application.

### Importing and Exporting Sighting Datas
After installing the prerequisite softwares mentioned above, we are going to import the 2018 Central Park Squirrel Census dataset.
```
python manage.py import_squirrel_data /path/to/file.csv 
#/path/to/file.csv is the location where 2018 Central Park Squirrel Census dataset is
```

Now the database already has the initial 3019 squirrels.

You can export all datas in the database to a .csv file at any time.
```
Python manage.py export_squirrel_data /path/to/file.csv  
# /path/to/file.csv is the location where you want to put the .csv file.
```
### Functions of this application.
* Showing a map that displays the location of the squirrel sightings on an [OpenStreets map](https://www.openstreetmap.org/about/). This uses the [leaflet](https://leafletjs.com/) library for plotting.
```
located at: /map
```
* Listing all squirrel sightings with linked to edit and add sightings.
```
located at: /sightings
```
* Updating a particular sighting
```
located at: /sightings/<unique-squirrel-id>
```
* Creating a new sighting
```
located at: /sightings/add
The following information are required when reporting a squirrel sighting: Latitude, Longitude, Unique Squirrel ID, Shift, Date, Age, Primary Fur Color, Location, Specific Location, Running, Chasing, climbing, eating, foraging, other activities, kuks, quaas, moans, tail flags, tal twitches, approaches, indifferent, runs from.
```
* Deleting a sighting
```
located at: /sightings/<unique-squirrel-is>
```
* Giving general stats about the sightings for you to decide, five of the attributes are listed.
```
located at: /sightings/stats
```

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [OpenStreetMap](https://www.openstreetmap.org/) - The plugin used for our map
* [Leaflet](https://leafletjs.com/) - The JavaScript library used to create an interactive maps

## Authors

* **Wensi Wang** - *Initial work*
* **Wenyi Xu** - *Initial work* 

## Acknowledgments

* Hat tip to Paul Logston for his guidance in this project.

