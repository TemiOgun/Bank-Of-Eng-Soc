from __future__ import unicode_literals

from django.db import models

class transaction(models.Model):
	number=models.IntegerField()
	title=models.CharField(max_length=50, unique=False)
	amount=models.FloatField()
	submitted=models.DateTimeField()
	processed=models.DateTimeField()
		
		
# Create your models here.
class account(models.Model):
	account_name = models.CharField(max_length=20, unique=True)
	account_pass = models.CharField(max_length=20, unique=True)
	

	

class message(models.Model): 
         
    name = models.CharField(max_length=100, unique=True) #Like a VARCHAR field
    description = models.TextField() #Like a TEXT field
    created = models.DateTimeField() #Like a DATETIME field
 
    def __unicode__(self): #Tell it to return as a unicode string (The name of the to-do item) rather than just Object.
        return self.name

class event(models.Model): #Table name, has to wrap models.Model to get the functionality of Django.
   
    name = models.CharField(max_length=100, unique=True) #Like a VARCHAR field
    created = models.DateTimeField() #Like a DATETIME field
 
    def __unicode__(self): #Tell it to return as a unicode string (The name of the to-do item) rather than just Object.
        return self.name
    
class alert(models.Model): #Table name, has to wrap models.Model to get the functionality of Django.
         
    name = models.CharField(max_length=100, unique=True) #Like a VARCHAR field
    description = models.TextField() #Like a TEXT field
    created = models.DateTimeField() #Like a DATETIME field
 
    def __unicode__(self): #Tell it to return as a unicode string (The name of the to-do item) rather than just Object.
        return self.name