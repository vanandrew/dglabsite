# Dosenbach Website Code

This is the backend for the Dosenbach Lab website.

#### Folder Structure

/dosenbach_lab: contains the django python package for the project  
/dlabsite: application for the dosenbach lab website  
/static: contains various static resources for apps, there are symlinks in each app folder that point to this folder

#### Overview

The code in this repository uses the [django](https://www.djangoproject.com/) framework.

The main files of interest are:  
* admin.py: contains the definitions for each model in the admin panel
* models.py: definitions for each data model
* urls.py: urls for each viewport
* views.py: defines views for each webpage (see .html files in templates folder)
