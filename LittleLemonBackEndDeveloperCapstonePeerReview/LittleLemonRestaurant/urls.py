from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views
from .views import BookingViewSet

router = DefaultRouter()
router.register(r'tables', BookingViewSet, basename='reservation')

urlpatterns = [path('', views.index, name='index'), path('restaurant/menu/items/', views.MenuItemView.as_view(), name='menu-items'),
    path('restaurant/menu/items/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-single-item'),
    path('restaurant/menu/category/', views.CategoryView.as_view()), path('restaurant/menu/orders/', views.OrderView.as_view()),
    path('restaurant/menu/cart/menu-items/', views.CartView.as_view()), path('restaurant/booking/', include(router.urls)), ]
