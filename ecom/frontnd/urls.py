from django. urls import path
from . import views

app_name = 'frontnd' 

urlpatterns = [

    path('home/', views.home, name='home'),
    path('myaccount/', views.myaccount, name="myaccount"),
    path('cart/', views.cart, name="cart"),
    path('category/', views.category, name="category"),
    path('product/<catname>', views.product, name='product'),
    path('singleproduct/<int:id>', views.singleproduct, name="singleproduct"),
    path('contact/', views.contact, name='contact'),
    path('userlogn/', views.userlogn, name='userlogn'),
    path('userlogout/', views.userlogout, name='userlogout'),
    path('cartdelete/<int:id>', views.cartdelete, name='cartdelete'),
    path('whish/', views.whish, name='whish'),

]
