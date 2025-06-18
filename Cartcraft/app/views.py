from django.shortcuts import render,redirect
from django.views import View
from .models import Costumer,Product,Order,Cart
from .forms import CustomerRegistrationForm
from django.contrib import messages
from .models import User

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

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')


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
