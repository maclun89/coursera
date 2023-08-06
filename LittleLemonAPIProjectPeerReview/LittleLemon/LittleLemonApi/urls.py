from django.urls import include, path
from . import views

urlpatterns = [
    path('', include('djoser.urls')),
    path('categories', views.CategoriesView.as_view()),
    path('menu-items', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('cart/menu-items', views.CartItemsView.as_view()),
    path('orders', views.OrdersView.as_view()),
    path('orders/<int:pk>', views.SingleOrderView.as_view()),
    path('groups/<str:group_name>/users', views.UsersView.as_view()),
    path('groups/<str:group_name>/users/<int:pk>', views.UsersView.as_view()),
]
