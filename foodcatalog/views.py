from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import User
# Create your views here.
from django.views.generic.edit import CreateView,UpdateView
from django.urls import reverse_lazy
from .models import Food,Cart
from .forms import CartCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.db.models import Sum
import datetime
def index(request):
    """View function for home page of site."""
    print(request.POST)	
    print(request.GET)
    print(request.user.username)
    # Generate counts of some of the main objects
    num_foods = Food.objects.all().count()
    #num_cartitems=Cart.objects.get()
    #print(num_cartitems)
    num_visits= request.session.get('num_visits',0)
    
    request.session['num_visits']= num_visits+1;
    context = {
        'num_foods': num_foods,'num_visits':num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic

class FoodListView(generic.ListView):
    model = Food

def FoodDetailView(request,my_id):
	obj=Food.objects.get(id=my_id)
	context={'object':obj}
	return render( request,'detail.html',context)
    

class Cartlist(LoginRequiredMixin,generic.ListView):
	model = Cart
	template_name ='cart_list.html'
	
	def get_queryset(self):
       	 return Cart.objects.filter(user=self.request.user).filter(created_at__range=(datetime.date.today(),datetime.date.today()+ datetime.timedelta(days=1))).order_by('created_at')
class AddFood(CreateView):
	model=Food
	fields='__all__'
class	UpdateFood(UpdateView):
	model=Food
	fields='__all__'

def CalorieCalculator(request):
	q=Cart.objects.filter(user=request.user).order_by('created_at')
	q=q.filter(created_at__range=(datetime.date.today(),datetime.date.today() + datetime.timedelta(days=1)))
	sumoffood=sum([f.food.calories for f in q])
	context={
	'sum':sumoffood,
	}
	return render(request,'caloriecalculator.html',context)
	
	
def user_Cart(request):
	
	
	form=CartCreateForm(request.POST or None)
	form.instance.user = request.user
	if form.is_valid():
		form.save()
	
	context={
	'form' : form,
	}
	
	return render(request,"cart_add.html",context)

def delete_view(request,my_id):
	obj=get_object_or_404(Cart,id=my_id)
	if(request.method=="POST"):
		obj.delete()
		redirect("../../")
	context={
	'object':obj
	}
	return render(request,'delete.html',context)
	 
from django.db.models import Q
def AddtoDiary(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(foodname__icontains=query) | Q(id__icontains=query)

            results= Food.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'addtodiaryfood.html', context)

        else:
            return render(request, 'addtodiaryfood.html')

    else:
        return render(request, 'addtodiaryfood.html')
#def calorie_calculator(request,count):
#	calorie_count=count
#	context={
#	'calorie':calorie_count
#	}
#	return render(request,'calorie.html',context)

	  
    
