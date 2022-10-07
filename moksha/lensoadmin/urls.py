
from django.urls import path
from . import views



urlpatterns = [

    path('admin_login',views.admin_login,name='admin_login'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('add_category',views.add_category,name='add_category'),
    path('admin_index',views.admin_index,name='admin_index'),

    

    path('add_products',views.add_products,name='add_products'),

    path('admin_category',views.admin_category,name='admin_category'),

    path('admin_product',views.admin_product,name='admin_product'),

    path('chart_details',views.chart_details,name='chart_details'),

    path('user_details',views.user_details,name='user_details'),
    path('admin_order_details',views.admin_order_details,name='admin_order_details'),
    path('single_user_details/<int:id>',views.single_user_details,name='single_user_details'),
    path('user_block/<int:id>',views.user_block,name='user_block'),
    path('user_unblock/<int:id>',views.user_unblock,name='user_unblock'),
    path('main_category_edit/<int:id>',views.main_category_edit,name='main_category_edit'),
    path('main_product_edit/<int:id>',views.main_product_edit,name='main_product_edit'),
    path('admin_order_details/<int:id>',views.admin_order_details,name='admin_order_details'),
    path('single_order_details/<order_number>/',views.single_order_details,name='single_order_details'),
    path('adminsearch/',views.adminsearch,name='adminsearch'),
    path('status_update/<order_number>/',views.status_update,name='status_update'),







   

    


]