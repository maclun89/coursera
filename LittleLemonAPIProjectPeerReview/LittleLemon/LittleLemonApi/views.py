from django.db.models import F
from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from .models import Category, MenuItem, Cart, Order, OrderItem
from .serializers import CategorySerializer, MenuItemSerializer, CartItemSerializer, OrderSerializer, UserSerializer
from .permissions import IsManager, IsDeliveryCrew
from datetime import date
from math import fsum


class DefaultResultsSetPagination(PageNumberPagination):
    page_size = None
    page_size_query_param = 'page_size'


class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.request.method != 'GET':
            return [IsManager()]
        else:
            return []

    def post(self, request, *args, **kwargs):
        try:
            Category.objects.create(
                slug=request.data['slug'],
                title=request.data['title']
            )
        except:
            return JsonResponse(status=400, data={'message': 'Bad request'})
        return JsonResponse(status=201, data={'message': 'Category created'})


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    filter_backends = [OrderingFilter]
    filterset_fields = ['category']
    ordering_fields = ['price', 'category']
    pagination_class = DefaultResultsSetPagination

    def get_permissions(self):
        if self.request.method != 'GET':
            return [IsManager()]
        else:
            return []

    def get_queryset(self):
        category = self.request.query_params.get("category", None)
        if category is None:
            return MenuItem.objects.all()
        else:
            return MenuItem.objects.filter(category=category)


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        if self.request.method != 'GET':
            return [IsManager()]
        else:
            return []

    def patch(self, request, *args, **kwargs):
        MenuItem.objects.filter(pk=self.kwargs['pk']).update(featured=~F('featured'))
        return JsonResponse(status=200, data={'message': 'Item updated'})


class CartItemsView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        menuitem = MenuItem.objects.get(pk=request.data['menuitem'])
        quantity = int(request.data['quantity'])
        unit_price = float(MenuItem.objects.get(pk=request.data['menuitem']).price)
        try:
            Cart.objects.create(
                user=request.user,
                menuitem=menuitem,
                quantity=quantity,
                unit_price=unit_price,
                price=unit_price * quantity
            )
        except:
            return JsonResponse(status=444, data={'message': 'Item already in cart'})
        return JsonResponse(status=201, data={'message': 'Item added'})

    def delete(self, request, *args, **kwargs):
        if request.data['menuitem']:
            try:
                Cart.objects.filter(user=request.user, menuitem=request.data['menuitem']).delete()
            except:
                return JsonResponse(status=404, data={'message': 'Item not in cart'})
            return JsonResponse(status=200, data={'message': 'Item removed'})
        else:
            try:
                Cart.objects.filter(user=request.user).delete()
            except:
                return JsonResponse(status=404, data={'message': 'No item in cart'})
            return JsonResponse(status=200, data={'message': 'All items removed'})


class OrdersView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    search_fields = ['user__username', 'delivery_crew__username']
    ordering_fields = ['total', 'date']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.groups.filter(name='Manager').exists():
            return Order.objects.all()
        elif self.request.user.groups.filter(name='Delivery crew').exists():
            return Order.objects.filter(delivery_crew=self.request.user)
        else:
            return Order.objects.filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        cart_items = Cart.objects.filter(user=request.user).values()
        if cart_items:
            total = fsum([float(item['price']) for item in cart_items])
            order = Order.objects.create(
                user=request.user,
                status=False,
                total=total,
                date=date.today()
            )
            for item in cart_items:
                menuitem = MenuItem.objects.get(pk=item['menuitem_id'])
                OrderItem.objects.create(
                    order=order,
                    menuitem=menuitem,
                    quantity=item['quantity'],
                    unit_price=item['unit_price'],
                    price=item['price']
                )
            Cart.objects.filter(user=request.user).delete()
            return JsonResponse(status=201, data={'message': 'Order placed'})
        else:
            return JsonResponse(status=404, data={'message': 'No item in cart'})


class SingleOrderView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method == 'PATCH':
            permission_classes = [IsManager | IsDeliveryCrew]
            return [permission() for permission in permission_classes]
        elif self.request.method == 'DELETE':
            return [IsManager()]
        elif self.request.method == "GET":
            # line 183 IsManager or IsDeliveryCrew or record.user == request.user
            return ""

    def patch(self, request, *args, **kwargs):
        if request.user.groups.filter(name='Manager').exists():
            delivery_crew = User.objects.get(username=request.data['delivery_crew'])
            Order.objects.filter(pk=self.kwargs['pk']).update(delivery_crew=delivery_crew)
            return JsonResponse(status=200, data={'message': 'Status updated'})
        elif request.user.groups.filter(name='Delivery crew').exists():
            Order.objects.filter(pk=self.kwargs['pk']).update(status=~F('status'))
            return JsonResponse(status=200, data={'message': 'Status updated'})

    def get(self, request, *args, **kwargs):
        try:
            record = Order.objects.get(id=kwargs["pk"])
            if IsManager or IsDeliveryCrew or record.user == request.user:
                data = self.serializer_class(record, read_only=True).data
                return JsonResponse(status=200, data={'data': data})
            return JsonResponse(status=403)
        except:
            return JsonResponse(status=404, data={'message': 'Order not found'})

class UsersView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsManager]

    def get_queryset(self):
        group_name = self.kwargs['group_name'].capitalize().replace("-", " ")
        return User.objects.filter(groups__name=group_name)

    def post(self, request, *args, **kwargs):
        group_name = self.kwargs['group_name'].capitalize().replace("-", " ")
        try:
            user = User.objects.get(username=request.data['username'])
            group = Group.objects.get(name=group_name)
            group.user_set.add(user)
            return JsonResponse(status=200, data={'message': 'User added to group'})
        except:
            return JsonResponse(status=404, data={'message': 'User not found'})


class SingleUserView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsManager]

    def get_queryset(self):
        group_name = self.kwargs['group_name'].capitalize().replace("-", " ")
        return User.objects.filter(groups__name=group_name)

    def delete(self, request, *args, **kwargs):
        group_name = self.kwargs['group_name'].capitalize().replace("-", " ")
        try:
            user = User.objects.get(id=self.kwargs['pk'])
            group = Group.objects.get(name=group_name)
            group.user_set.remove(user)
        except:
            return JsonResponse(status=404, data={'message': 'User not found'})
        return JsonResponse(status=200, data={'message': 'User removed from group'})
