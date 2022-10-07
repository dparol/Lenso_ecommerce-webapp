from cmath import rect
from contextlib import contextmanager, redirect_stderr
from email import message
import email
from email.policy import default
from itertools import product
from multiprocessing import context
from django.views.decorators.cache import never_cache

from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import User
from mkhome.forms import RegistrationForm,UserForm,UserProfileForm


from .models import Account, UserProfile 
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required


from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

from store.models import Product
from category.models import Category
from carts.models import Cart, CartItem 
from carts.views import _cart_id
import requests

from orders.models import Order, OrderProduct,OrderStatus





# # Create your views here.




@never_cache
def home(request):
    products=Product.objects.all().filter(is_available=True)
    product_count = products.count()
    context={
        'products':products,
        'product_count':product_count,
    }
    return render(request,'mkhome/index.html',context)



def register(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name =form.cleaned_data['first_name']
            last_name =form.cleaned_data['last_name']
            email =form.cleaned_data['email']
            phone_number =form.cleaned_data['phone_number']
            password =form.cleaned_data['password']
            username=email.split('@')[0]
            user=Account.objects.create_user(first_name=first_name,last_name=last_name,email=email,password=password,username=username)
            user.phone_number=phone_number
            user.save()

            #USER ACTIVATION
            current_site = get_current_site(request)
            mail_subject='Please activate your account'
            message = render_to_string('mkhome/account_verification_email.html',{
                'user':user,
                'domain':current_site,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':default_token_generator.make_token(user),
            })
            to_email=email
            send_email=EmailMessage(mail_subject,message,to=[to_email])
            send_email.send()
            # return redirect(register)
           
            return redirect('login/?command=verification&email='+email)

    else:
        form=RegistrationForm()
    context={
        'form':form
    }
    return render(request,'mkhome/register21.html',context)



def  login(request):
    if request.method == 'POST':
        
        email=request.POST['email']
        password=request.POST['password']
        user=auth.authenticate(request,email=email,password=password)
        print("here okay")

        
        if user is not None:
            
                try:
                    cart = Cart.objects.get(cart_id=_cart_id(request))
                    is_cart_item_exists=CartItem.objects.filter(cart=cart).exists()
                    print(is_cart_item_exists)
                    if is_cart_item_exists:
                        cart_item =CartItem.objects.filter(cart=cart)

                        product_variation=[]
                        for item in cart_item:
                            variation = item.variation.all()
                            product_variation.append(list(variation))

                        cart_item = CartItem.objects.filter(user=user)

                        ex_var_list =[]
                        id=[]
                        for item in cart_item:
                            existing_variation = item.variations.all()
                            ex_var_list.append(list(existing_variation))
                            id.append(item.id)

                        for pr in product_variation:
                            if pr in ex_var_list:
                                index= ex_var_list.index(pr)
                                item_id=id(index)
                                item=CartItem.objects.get(id=item_id)
                                item.quantity += 1
                                item.user = user
                                item.save()
                            else:
                                cart_item =CartItem.objects.filter(cart=cart)
                                for cart in cart_item:
                                    item.user = user
                                    item.save()
                except:
                    pass
                
                auth.login(request, user)
                # messages.success(request, 'you are logged in.')
                url = request.META.get('HTTP_REFERER')
                try:
                   query  = requests.utils.urlparse(url).query
                   params = dict(x.split('=') for x in query.split('&'))
                   if 'next' in params:
                       return redirect(params['next'])
                
                except:
                    return redirect('/')
        else:
            messages.error(request, "Invalid login credentials")
            return redirect('login')    
    return render(request,'mkhome/login.html')


@login_required(login_url='login') 
def logout(request):
    auth.logout(request)
    messages.success(request,'you are logged out')
    return redirect(home)


        
def activate(request,uidb64,token):
    try:
        uid=urlsafe_base64_decode(uidb64).decode()
        user =Account._default_manager.get(pk=uid)
    except(TypeError,ValueError,OverflowError,Account.DoesNotExist):
        user=None
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active =True
        user.save()
        messages.success(request,'congratulations your account is activated.')
        return redirect('login')
    else:
        messages.error(request,'invalid activation link')
        return redirect('register')


@never_cache
def forgotpassword(request):
    if request.method == 'POST':
        email=request.POST['email']
        if Account.objects.filter(email=email).exists():
            user=Account.objects.get(email__exact=email)    


            current_site = get_current_site(request)
            mail_subject='Please reset your password'
            message = render_to_string('reset_password_email.html',{
                'user':user,
                'domain':current_site,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':default_token_generator.make_token(user),
            })
            to_email=email
            send_email=EmailMessage(mail_subject,message,to=[to_email])
            send_email.send()
            messages.success(request,'password reset email has been sent to your email address.')
            return redirect('login')
        else:
            messages.error(request,'Account does not exist')
            return redirect('forgotpassword')
    return render(request,'forgotpassword.html')    
@never_cache    
def resetpassword_validate(request,uidb64,token):
    try:
        uid=urlsafe_base64_decode(uidb64).decode()
        user =Account._default_manager.get(pk=uid)
    except(TypeError,ValueError,OverflowError,Account.DoesNotExist):
        user=None
    if user is not None and default_token_generator.check_token(user,token):
        request.session['uid'] = uid
        messages.success(request,'pleace reset your password.')
        return redirect('resetpassword')
    else:
        messages.error(request,'the link has been expired')
        return redirect('login')


@never_cache  

def resetpassword(request):
    if request.method=='POST':
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']

        if password == confirm_password:
            uid = request.session.get('uid')
            user=Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request,'password reset successful')
            return redirect('login')
        else:
            messages.error(request,'password do not match!')
            return redirect('resetpassword')
    else:
        return render(request,'resetpassword.html')
    


def dashboard(request,id):
    orders=Order.objects.order_by('-created_at').filter(user_id=request.user.id,is_ordered=True)
    orders_count =orders.count()
    context={
        'orders_count':orders_count,
        # 'rect_products':rect_products,
    }
    return render(request,'mkhome/dashboard.html',context)

def my_orders(request):
    orders=Order.objects.filter(user=request.user,is_ordered=True).order_by('-created_at')
    context={
        'orders':orders
    }
    return render(request,'mkhome/my_orders.html',context)

@login_required(login_url='login') 
def edit_profile(request):
    
    userprofile=UserProfile.objects.filter(user=request.user)    
    
    if request.method=='POST':
        user_form=UserForm(request.POST,instance=request.user)
        profile_form=UserProfileForm(request.POST,request.FILES,instance=request.user)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,"your profile has been edited")
            return redirect('edit_profile')
    else:
        user_form=UserForm(instance=request.user)
        profile_form=UserProfileForm(instance=request.user)
        context={
            'user_form':user_form,
            'profile_form':profile_form,
        }


    return render(request,'mkhome/edit_profile.html',context)



def change_password(request):
    if request.method == 'POST':
        current_password=request.POST['current_password']
        new_password=request.POST['new_password']
        confirm_password=request.POST['confirm_password']

        

        if new_password == confirm_password:
            user=Account.objects.get(username__exact=request.user.username)
            success=user.check_password(current_password)
            if success:
                user.set_password=new_password
                user.save()
                messages.success(request," your password has been changed")
                return redirect('change_password')
            else:
                messages.error(request,'please enter a valid new password')
                return redirect('change_password')
        else:
            messages.error(request,'the passwords does not match')
            return redirect('change_password')
    return render(request,'mkhome/change_password.html')


def order_detail(request,order_id):
    order_detail =OrderProduct.objects.filter(order__order_number=order_id)
    order=Order.objects.get(order_number=order_id)
    context={
        'order_detail':order_detail,
        'order':order,
    }

    return render(request,'mkhome/order_detail.html')

def shop(request):
    products=Product.objects.all().filter(is_available=True)
    product_count = products.count()
    context={
        'products':products,
        'product_count':product_count,
    }

    return render(request,'mkhome/shop.html',context)


def contact(request):
    return render(request,'mkhome/contact.html')


def order_summery(request,order_number):

    summery=OrderProduct.objects.filter(order__order_number=order_number)
   
 

   
    context={
        'summery':summery,
        'order_number':order_number
        
    }
    return render(request,'mkhome/summery.html',context)

# def Recent_Products(request):
    
#     rect_products = Product.objects.order_by(-id)

#     context = {
#         "rect_products" : rect_products
#     }

#     return render(request,'mkhome/base.html', context)

# for pro in rect

# pro.id 
# pro.name






# def user_login(request):

#     if request.user.is_authenticated:
#         return redirect(home) 

#     if request.method == 'POST':
#         username=request.POST['username']
#         password=request.POST['password']
#         user=authenticate(request,username=username,password=password)
        
#         if user is not None:
#             if user.is_superuser:
#                 login(request,user)
#                 return redirect(admin_index)
#             else:       
#                 login(request,user)
#                 return redirect('home')
        
#         else:
#             message.info(request,'enter a valid username or password')
#     return render(request,'login.html')

# def user_logout(request):
#     logout(request)
#     return redirect('home')

# def user_register(request):
#     if request.user.is_authenticated:
#         return redirect('home')
#     else:
#         form=create_user()
#         if request.method == 'POST':
#             form=create_user(request.POST)
#             if form.is_valid():
#                 form.save()
#                 user=form.cleaned_data.get('username')
#                 messages.success(request,'account successfully created'+user)
#                 return redirect(user_verify)
#         context={
#             'form':form
#         }
#         return render(request,'register.html',context)

           

# def index(request):
#     return render(request,'index.html')


# def user_verify(request):
#     return render(request,'verify.html')













        






