from __future__ import unicode_literals

from django.db import models

# Create your models here.
class account(models.Model):
	account_name = models.CharField(max_length=20, unique=True)
	account_pass = models.CharField(max_length=20, unique=True)
	

class transaction(models.Model):
	number=models.IntegerField()
	title=models.CharField(max_length=20,unique=False)
	amount=models.DecimalField(...,max_digits=10,decimal_places=2)
	submitted=models.DateTimeField()
	processed=models.DateTimeField()
	
	def __unicode__(self):
		return self.title
	

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