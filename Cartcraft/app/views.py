from django.shortcuts import render,redirect
from django.views import View
from .models import Costumer,Product,Order,Cart
from .forms import CustomerRegistrationForm,CustomerProfileForm
from django.contrib import messages
from .models import User
from difflib import SequenceMatcher


#Product
class ProductView(View):
    def get(self, request):
        mobiles = Product.objects.filter(category='M')
        laptops = Product.objects.filter(category='L')
        context = {
            'mobiles': mobiles,
            'laptops': laptops,
        }
        return render(request, 'app/home.html', context)
#Product
class Product_detail(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk) 
        return render(request,'app/productdetail.html',{'product':product})    


def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

class ProfileView(View):
    def get(self, request):
        try:
            profile = Costumer.objects.get(user=request.user)
            form = CustomerProfileForm(instance=profile)
        except Costumer.DoesNotExist:
            form = CustomerProfileForm()
        return render(request, 'app/profile.html', {'form': form, 'active': 'btn-primary'})

    def post(self, request):
        try:
            profile = Costumer.objects.get(user=request.user)
            form = CustomerProfileForm(request.POST, instance=profile)
        except Costumer.DoesNotExist:
            form = CustomerProfileForm(request.POST)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, "Your profile has been updated successfully ✅")
            return redirect('profile')

        return render(request, 'app/profile.html', {'form': form, 'active': 'btn-primary'})
    
 #Search
def search_view(request):
    query = request.GET.get('q', '').strip()

    if not query:
        return redirect('home')

    # Basic case-insensitive partial match
    results = Product.objects.filter(title__icontains=query)
    exact_match = results.filter(title__iexact=query).first()
    if exact_match and results.count() == 1:
        return redirect('product-detail', pk=exact_match.pk)

    return render(request, 'app/search_results.html', {'query': query, 'results': results})





        

def address(request):
    add=Costumer.objects.get(user=request.user)
    return render(request, 'app/address.html',{'add':add})

def orders(request):
 return render(request, 'app/orders.html')

#Mobiles
def mobile(request, data=None):
    if data is None:
        mobile = Product.objects.filter(category='M')
    elif data in ['Xiaomi', 'Samsung', 'Apple', 'OPPO', 'Vivo']:
        mobile = Product.objects.filter(category='M', brand=data)
    else:
        mobile = Product.objects.none()
    return render(request, 'app/mobile.html', {'mobiles': mobile})

#laptops
def laptop(request, data=None):
    if data is None:
        laptops = Product.objects.filter(category='L')
    elif data in ['HP', 'DELL', 'LENOVO',]:
        laptops = Product.objects.filter(category='L', brand=data)
    else:
        laptops = Product.objects.none()
    return render(request, 'app/laptop.html', {'laptops': laptops})

#Costumer Registration
class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form': form})
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            # Check if email already exists
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists.')
                return render(request, 'app/customerregistration.html', {'form': form})
            form.save()
            messages.success(request, 'Registration successful!')
            return redirect('login')
        return render(request, 'app/customerregistration.html', {'form': form})


            

def checkout(request):
 return render(request, 'app/checkout.html')
