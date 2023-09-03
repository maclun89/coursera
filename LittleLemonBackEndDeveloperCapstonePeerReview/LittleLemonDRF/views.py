from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import OrderItemSerializer,OrderSerializer,CartSerializer,MenuItemSerializer,CategorySerializer
from .models import OrderItem,Order,Cart, MenuItem,Category
from .permissions import IsDeliveryCrew, IsManager
# class RatingsView(generics.ListCreateAPIView):
#     queryset = Rating.objects.all()
#     serializer_class = RatingSerializer


#     def get_permissions(self):
#         if self.request.method == "GET":
#             return []

#         return [IsAuthenticated()]
class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated,IsManager]
    
class MenuItemView(generics.RetrieveAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    
class OrderView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
class CartView(generics.ListCreateAPIView, generics.UpdateAPIView,generics.DestroyAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
