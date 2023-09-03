from django.urls import path,include
from . import views

urlpatterns = [
path("ratings", views.RatingsView.as_view()),
path('category/',views.CategoryView.as_view()),
path('menu-items/',views.MenuItemsView.as_view()),
path('menu-items/<int:id>/',views.MenuItemView.as_view()),
path('orders/',views.OrderView.as_view()),
path('cart/menu-items/',views.CartView.as_view()),

path('', include('djoser.urls')),
path('', include('djoser.urls.authtoken')),
]
