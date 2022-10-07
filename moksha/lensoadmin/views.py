import contextlib
from unicodedata import category
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages,auth
from mkhome.models import Account,MyAccountManager,UserProfile
from store.models import Product,VariationManager,Variation
from orders.models import *
from category.models import Category

from .forms import AddProduct,AddCategory,Admin_Orderstatus
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.db.models import Q


# Create your views here.
@login_required(login_url='login')
def admin_home(request):
    if request.user.is_superadmin:
        single_orders=OrderProduct.objects.all()
        context={
        
                 'single_orders':single_orders,
                }
        return render(request, 'lensoadmin/admin_index.html',context)


  
    return HttpResponse('You are not authorized to view this page')

@login_required(login_url='login')
def admin_login(request):
    if request.user.is_authenticated:
        return redirect('admin_home')

    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']

        user=auth.authenticate(request,email=email,password=password)
        if user is not None:
            user = Account.objects.get(email=email)
            if user.is_admin == True:
                login(request,user)
                return redirect('admin_home')
            else:
                messages.error(request,'user is not found')
                return redirect('admin_login')
        else:
            messages.error(request,'user is not found')
    return render(request,'lensoadmin/admin_login.html')
@login_required(login_url='login')
def admin_index(request):
    return render(request,'lensoadmin/admin_index.html')


@login_required(login_url='login')
def user_block(request, id):
    if request.user.is_superadmin:
        user = Account.objects.get(id=id)
        user.is_active = False
        user.save()
        return redirect('user_details')
    return HttpResponse('You are not authorized to view this page')



@login_required(login_url='login')
def user_unblock(request, id):
    if request.user.is_superadmin:
        user = Account.objects.get(id=id)
        user.is_active = True
        user.save()
        return redirect('user_details')
    return HttpResponse('You are not authorized to view this page')

@login_required(login_url='login')
def admin_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,'successfully logout')
    return redirect('admin_login')

@login_required(login_url='login')
def add_category(request):
    if request.method=='POST':
        form=AddCategory(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(add_category)
        else:
            messages.info(request,'please fill correct values')
    else:
        form=AddCategory()

    context={
        'form':form
    }
    
    return render(request,'lensoadmin/add_category.html',context)
@login_required(login_url='login')
def main_category_edit(request,id):
    if request.user.is_superadmin:
        main = Category.objects.get(id=id)
        
        form = AddCategory(instance=main)
        
        if request.method == 'POST':
            form = AddCategory(request.POST, instance=main)
            if form.is_valid():
                form.save()
                return redirect('add_category')
            else: 
                print(form.errors)

        context = {
            'main': main,
            'form': form,
           
        }
        return render(request, 'lensoadmin/edit_category.html', context)
    
    return HttpResponse('You are not authorized to view this page')

@login_required(login_url='login')
def main_product_edit(request,id):
    if request.user.is_superadmin:
        main = Product.objects.get(id=id)
        
        form = AddProduct(instance=main)
        
        if request.method == 'POST':
            form = AddProduct(request.POST, instance=main)
            if form.is_valid():
                form.save()
                return redirect('add_products')
            else: 
                print(form.errors)

        context = {
            'main': main,
            'form': form,
           
        }
        return render(request, 'lensoadmin/edit_product.html', context)
    
    return HttpResponse('You are not authorized to view this page')

@login_required(login_url='login')
def admin_order_details(request):
    order = Order.objects.all()
    payment=Payment.objects.all()
    print(payment)

    print(order)
    context = {
        "order": order,
        'payment':payment}
    return render(request,'lensoadmin/admin_order_details.html',context)


@login_required(login_url='login')
def add_products(request):
    if request.method == 'POST':
        form =AddProduct(request.POST,request.FILES)
        if form.is_valid():
            print('valid')
            form.save()
            print('data saved successfully')
            return redirect(add_products)
        else:
            print(form.errors)
            messages.info(request,'product not added')
    else:
        form =AddProduct()
     
    return render(request,'lensoadmin/add_products.html',{'form':form})

@login_required(login_url='login')
def admin_category(request):
    category=Category.objects.all()
    context={
        'category':category
    }
    return render(request,'lensoadmin/admin_category.html',context)


@login_required(login_url='login')
def admin_product(request):
    products=Product.objects.all()
    context={
        'products':products
    }
    return render(request,'lensoadmin/admin_products.html',context)


@login_required(login_url='login')
def chart_details(request):
    return render(request,'lensoadmin/chart_details.html')


@login_required(login_url='login')
def user_details(request):

    user_details=Account.objects.all()
    context={
        'user_details':user_details
    }
    return render(request,'lensoadmin/user_details.html',context)

@login_required(login_url='login')
def single_user_details(request,id):
     order=[]
     if request.user.is_admin:
        user = Account.objects.get(id=id)
        order= OrderProduct.objects.filter(user__id=user.id)
        
        print(user)
        print(order)
        context = {
            'user': user,
            'order':order,
        }
        return render(request,'lensoadmin/single_user_details.html',context)

def admin_order_details(request):
    orders=Order.objects.all()
  
    context={
        'orders':orders,
      
    }

    return render(request,'lensoadmin/admin_order_details.html',context)

def single_order_details(request,order_number):
    single_orders=OrderProduct.objects.filter(order__order_number=order_number)
    context={
        
        'single_orders':single_orders,
    }
    return render(request,'lensoadmin/single_order_details.html',context)

def adminsearch(request):
    if 'keyword' in request.GET:
        keyword =request.GET['keyword']
        user=['USER','user','User']
        product=['Product','product','PRODUCT']
        category=['category','Category','CATEGORY']
        if keyword:
            if keyword in user:
                return redirect('user_details')
            elif keyword in product:
                return redirect('admin_product')
            elif keyword in category:
                return redirect('admin_category')
            else:
                return render(request,'lensoadmin/admin_index.html')

    return render(request,'lensoadmin/admin_index.html')


def status_update(request,order_number):
    order=[]

    
    
    if request.method == 'POST':
        # form=Admin_Orderstatus(instance=payment_id)
        form =Admin_Orderstatus(request.POST,request.FILES)
        if form.is_valid():
            
            form.save()
            order=Order.objects.get(order_number=order_number)
            # order=Order.objects.get(payment__payment_id=payment_id)
            print(order)
            if form.cleaned_data['Cancelled']:
                order.order_status = 'Cancelled'
                order.save()
            elif form.cleaned_data['delivered']:
                order.order_status = 'Delivered'
                order.save()
            elif form.cleaned_data['Shipped']:
                order.order_status = 'On shipping'
                order.save()
            elif form.cleaned_data['order_confirmed']:
                print('inside confirm')
                order.order_status = 'Ready to ship'
                order.save()
                print('saved')

            elif form.cleaned_data['Accepted']:
                order.order_status = 'Accepted'
                order.save()
            return redirect('admin_home')



            
        else:
            print(form.errors)
            messages.info(request,'no changes')
    else:
        form =Admin_Orderstatus()
    # except (Payment.DoesNotExist, Order.DoesNotExist):
    #     return redirect('/')


    return render(request,'lensoadmin/status_update.html',{'form':form})




    