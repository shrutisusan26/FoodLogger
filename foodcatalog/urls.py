from django.urls import path
from .views import FoodDetailView,index,FoodListView,Cartlist,AddtoDiary,user_Cart,CalorieCalculator,delete_view,AddFood

urlpatterns = [
    path('', index, name='index'),
    path('foods/', FoodListView.as_view(), name='foods'),
    path('food/<int:my_id>', FoodDetailView, name='food-detail'),
    
]
urlpatterns += [  
   
     path('food/create/',Cartlist.as_view(), name='cart_list'),
     path('food/foodadd/',AddFood.as_view(),name='add-food'),
     path('food/foodupdate/<int:id>',AddFood.as_view(),name='food-update'),
     path('food/add/', user_Cart, name='cart-add'),
     path('food/calorie/',CalorieCalculator,name='cart-calorie'), 
     path('food/delete/<int:my_id>/',delete_view,name="deleteview"),  
]
urlpatterns += [  
    path('food/addtoday/', AddtoDiary, name='addtodiary'),
    
]
