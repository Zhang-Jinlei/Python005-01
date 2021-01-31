from django.db import models

# Create your models here.
from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager, User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


class Orders(models.Model):
    """
    订单
    """
    __tablename__ = 'orders'
    title = models.CharField(max_length=30, verbose_name='订单标题', default='')
    body = models.CharField(max_length=30, verbose_name='订单内容', default='')
    create_time = models.DateTimeField(auto_now_add=True)  # 订单创建时间
    owner = models.ForeignKey(
        'auth.User', verbose_name='用户id', related_name='orders', on_delete=models.CASCADE)

    class Meta:
        ordering = ['create_time']

    def __str__(self):
        return self.title

