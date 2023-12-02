from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
path('admin/', admin.site.urls),
path('',views.indexpage,name='indexpage'),
path('productlist/<int:myid>',views.productlist,name='productlist'),
path('productdetail/<int:pid>',views.productdetail,name='productdetail'),
]