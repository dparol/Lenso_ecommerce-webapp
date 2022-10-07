from django import forms
from orders.models import Order

from store.models import Product
from autoslug import AutoSlugField
from category.models import Category
from orders.models import OrderStatus





class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"


class AddProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields =  ['product_name', 'description', 'brand', 'price', 'old_price', 'images', 'stock', 'is_available', 'category']
        widgets = {
              'product_name': forms.TextInput(attrs={'class':"form-control border border-danger text-light", 'placeholder':"product name"}),
              'description': forms.Textarea(attrs={'class':"form-control  border border-danger text-light", 'placeholder':"Product Description" }),
              'brand': forms.TextInput(attrs={'class':"form-control  border border-danger text-light", 'placeholder':"brand"}),
              'price': forms.NumberInput(attrs={'class':"form-control  border border-danger text-light", 'placeholder':"current price"}),
              'old_price': forms.NumberInput(attrs={'class':"form-control  border border-danger text-light", 'placeholder':"current price"}),
              'images': forms.ClearableFileInput(),
              'stock': forms.NumberInput(attrs={'class':"form-control  border border-danger text-light", 'placeholder':"Stock", 'min':'0'}),
              'is_available': forms.CheckboxInput(),
              'category' : forms.Select(attrs={'class':"form-select  border border-danger text-light", 'placeholder':"product name"}),
            }
        
class AddCategory(forms.ModelForm):
    class Meta:
        model=Category
        fields =['category_name', 'description', 'cat_image']
        widgets = {
              'category_name': forms.TextInput(attrs={'class':"form-control border border-danger text-light", 'placeholder':"category name"}),
              
              ' description': forms.Textarea(attrs={'class':"form-control  border border-danger text-light", 'placeholder':"category Description" }),
              'cat_image': forms.ClearableFileInput(),
              }

class Admin_Orderstatus(forms.ModelForm):
    class Meta:
        model=OrderStatus
        fields=['order','order_confirmed', 
        'order_confirmed_date', 
        'Shipped','Shipped_date', 'out_for_delivery_date', 
        'out_for_delivery', 'delivered', 
        'delivered_date', 'Cancelled', 
        'cancelled_date','is_active']
        widgets = {
              'order': forms.Select(attrs={'class':"form-select  border border-danger text-light", 'placeholder':"order name"}),
              'order_confirmed': forms.CheckboxInput(),
              'order_confirmed_date': forms.SelectDateWidget(),
              'Shipped': forms.CheckboxInput(),
              'Shipped_date': forms.SelectDateWidget(),
              'out_for_delivery': forms.CheckboxInput(),

              'out_for_delivery_date': forms.SelectDateWidget(),
              'delivered': forms.CheckboxInput(),
              'delivered_date':forms.SelectDateWidget(),
              'Cancelled': forms.CheckboxInput(),
              'cancelled_date' : forms.SelectDateWidget(),
              'is_active' : forms.CheckboxInput(),

            }
