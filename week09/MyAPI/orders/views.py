from django.shortcuts import render

# Create your views here.


from orders.models import Orders
from orders.serializers import OrdersSerializer
from rest_framework import viewsets, permissions
from rest_framework.request import Request
from rest_framework.response import Response
from orders.permissions import IsOwnerOrReadOnly
# from django.contrib.auth.models import
from django.contrib.auth import get_user_model

User = get_user_model()
from orders.serializers import UserSerializer, CreateOrderSerializer
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse


class OrderAPIViewSet(viewsets.ModelViewSet):
    """
    使用serializers和viewset
    """
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class OrderCreateAPIViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = CreateOrderSerializer

    def retrieve(self, request, pk=None):
        """ 用户详情 """
        # 获取实例
        user = self.get_object()

        # 序列化
        serializer = self.get_serializer(user)
        data = serializer.data
        return Response(data)

    def list(self, request: Request, *args, **kwargs):
        """ 获取用户列表 """
        return Response([])

    def create(self, request, *args, **kwargs):
        """
        创建用户
        """

        serializer = CreateOrderSerializer(data=request.data, context={'request': request})
        # print(request.data['username'])
        # save 前必须先调用 is_valid()
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, pk=None):
        """ 用户详情 """
        # 获取实例
        user = self.get_object()

        # 序列化
        serializer = self.get_serializer(user)
        return Response(serializer.data)



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-detail', request=request, format=format),
        'orders': reverse('orders-detail', request=request, format=format),
        'orders/create': reverse('orders_create_list', request=request, format=format),
    })
