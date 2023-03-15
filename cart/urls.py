from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<int:item_id>/', views.add_to_cart, name='cart_add'),
    path('adjust/<int:item_id>/', views.adjust_cart, name='cart_adjust'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='cart_remove'),
]