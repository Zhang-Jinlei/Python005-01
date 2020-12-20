from django.urls import path, re_path, register_converter
from . import views

# register_converter(converters.IntConverter, 'myint')
# register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('index', views.index),

]
