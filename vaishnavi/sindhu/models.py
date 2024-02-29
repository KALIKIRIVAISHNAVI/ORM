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

