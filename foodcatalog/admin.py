from django.contrib import admin

# Register your models here.

from .models import Food
from .models import Cart

#admin.site.register(Food)
#admin.site.register(Cart)
@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
	list_display=('foodname','quantity','calories','fats','carbs','proteins')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
	list_display=('food','created_at','user')
	
