#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Describe :
# @Time     : 2021/1/30 8:33 PM
# @Author   : Zhang JinLei
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from orders import views
from django.conf.urls import include
from rest_framework.documentation import include_docs_urls

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'orders', views.OrderAPIViewSet)
router.register(r'orders/create', views.OrderCreateAPIViewSet, 'orders_create_list')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
    path('docs', include_docs_urls(title='Orders')),
]
