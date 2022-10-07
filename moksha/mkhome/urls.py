
from django.urls import path
from . import views




urlpatterns = [

   
    path('home/',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('register',views.register,name='register'),
    path('activate/<uidb64>/<token>/',views.activate,name='activate'),
    path('forgotpassword',views.forgotpassword,name='forgotpassword'),
    path('dashboard/<int:id>',views.dashboard,name='dashboard'),
    path('resetpassword_validate/<uidb64>/<token>/',views.resetpassword_validate,name='resetpassword_validate'),
    path('resetpassword',views.resetpassword,name='resetpassword'),
   
    
   
    path('',views.home,name='index'),
    path('my_orders/',views.my_orders,name='my_orders'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('change_password/',views.change_password,name='change_password'),
    path('order_detail/<int:order_id>',views.order_detail,name='order_detail'),
    path('shop',views.shop,name='shop'),
    path('contact',views.contact,name='contact'),
    path('my_orders/order_summery/<order_number>/',views.order_summery,name='order_summery'),








    
    
]