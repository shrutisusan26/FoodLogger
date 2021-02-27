from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.urls import reverse  # To generate URLS by reversing URL patterns
from django.db.models.signals import post_save
from django.dispatch import receiver 
from datetime import datetime
class Food(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    foodname = models.CharField(max_length=200)
    quantity=models.IntegerField(help_text='Enter in cups or whole numbers')
    calories=models.IntegerField()
    fats=models.IntegerField(help_text='Enter in grams')
    carbs=models.IntegerField(help_text='Enter in grams')
    proteins=models.IntegerField(help_text='Enter in grams')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.foodname

    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('food-detail', args=[str(self.id)])

class Meta:
    ordering = ['foodname']

class Cart(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
	meal=models.CharField(max_length=20, help_text='Enter the meal you want to eat',blank=True,null=True)
	food=models.ForeignKey('Food', on_delete=models.SET_NULL, null=True) 
	created_at = models.DateTimeField(default=datetime.now)
	
	def __str__(self):
        
        	return self.meal

	@property
	def is_nextday(self):
	    if date.today() > created_at :
	       return True
	    return False
	




 
