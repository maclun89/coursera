from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('items/', views.MenuItemView.as_view(), name='menu-items'),
    path('items/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-single-item'),
    path('category/',views.CategoryView.as_view()),
    path('orders/',views.OrderView.as_view()),
    path('cart/menu-items/',views.CartView.as_view()),

]