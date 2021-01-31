# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework import serializers
from orders.models import Orders


class OrdersSerializer(serializers.HyperlinkedModelSerializer):
    """订单序列"""
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Orders
        fields = ['url', 'id', 'body', 'create_time', 'owner', 'title']


class CreateOrderSerializer(serializers.HyperlinkedModelSerializer):
    """创建用户序列"""
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Orders
        fields = ['url', 'id', 'owner', ]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """用户序列"""
    orders = serializers.PrimaryKeyRelatedField(many=True, queryset=Orders.objects.all())
    # orders = OrdersSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'orders', ]



