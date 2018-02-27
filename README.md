# Item Catalog #


## Overview
> A web application that provides a list of clothing items within a variety of categories. The app also implements a third-party authentication & authorization service (Google and Facebook accounts). Signed-in users have the ability to create, edit and delete their own categories and items.

## Built with 

  * Python
  * [Flask](http://flask.pocoo.org)
  * [SQLAlchemy](http://www.sqlalchemy.org)
  * HTML/CSS/JavaScript
  * Jinja2
  * OAuth (Google & Facebook)
  * Materialize.js

## Set Up

#### 1. Install [Vagrant](https://www.vagrantup.com/downloads.html) and [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

#### 2. Clone the vagrantfile from Udacity repo: [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm)

#### 3. Launch the Virtual Machine:

From your terminal, inside the vagrant subdirectory, run the command

    vagrant up

When finished, run

    vagrant ssh

to log in to the newly installed Linux VM

#### 4. Clone this repo into vagrant subdirectory. 

#### 5. Populate the database

cd into the vagrant directory and use the command

    python lotsofclothes.py

#### 6. Run application 

Withint the same directory, use the command 

    python project.py

#### 7. Access and test application by visiting http://localhost:5000 locally

## API Endpoints

  * /catalog/JSON
    * Shows information on all categories.

  * /catalog/<int:category_id>/items/JSON
    * Shows information for all items in category corresponding to *category_id*.

  * /catalog/<int:category_id>/<int:item_id>/JSON
    * Shows information for a specific item corresponding to *item_id* within category specificed by *category_id*.

## Project Display 

## Sources & References 
  * Udacity - Full Stack Developer Nanodegree
    * [Full Stack Foundation](https://classroom.udacity.com/courses/ud088)
    * [Authentication & Authorization](https://classroom.udacity.com/courses/ud330/lessons/3960758610/concepts/39804189050923)
  * All items used to populate database in lotsofclothes.py are from [farfetch](www.farfetch.com)


    



