# Ex02 Django ORM Web Application
## Date: 29-02-2024

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## Entity Relationship Diagram
![Alt text](<Screenshot 2024-02-29 141941.png>)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

```
models.py

from django.db import models
from django.contrib import admin
class Book(models.Model):
   bookid=models.IntegerField(primary_key=True);
   bookname=models.CharField(max_length=50);
   authorname=models.CharField(max_length=50);
   dateofpublication=models.DateField();
   pictureofauthor=models.FileField(help_text="Upload Picture in PDF");
class BookAdmin(admin.ModelAdmin):
   list_display=("bookid","bookname","authorname","dateofpublication","pictureofauthor");

```
```
admin.py

from django.contrib import admin
from .models import Book,BookAdmin
admin.site.register(Book,BookAdmin)
```

## OUTPUT

![Alt text](<Screenshot (77).png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
