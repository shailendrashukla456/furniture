from django.urls import path
from my_shop import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('about/', views.about, name='about'), 
    path('services',views.services,name="services"),
    path('contact', views.contact, name='contact'),
    path('products', views.products, name='products'),
    path('clients',views.clients,name='clients')

]