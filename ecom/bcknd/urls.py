from django.urls import path
from . import views

app_name = 'bcknd'

urlpatterns = [ 
    path('data/', views.data, name='data'),
    path('display/', views.display, name='display'),

    path('index/', views.index, name='index'),
    path('catedata/', views.catdata, name='catedata'),
    path('catedisplay/', views.catedisplay, name='catedisplay'),
    path('catedelete/<int:id>', views.catedelete, name='catedelete'),

    path('prodata/', views.prodata, name='prodata'),
    path('prodisplay/', views.prodisplay, name='prodisplay'),
    path('prodelete/<int:id>', views.prodelete, name='prodelete'),
    path('usrcontact/', views.usrcontact, name='usrcontact'),
    path('usrcontactdelete/<int:id>', views.usrcontactdelete, name='usrcontactdelete'),
]
