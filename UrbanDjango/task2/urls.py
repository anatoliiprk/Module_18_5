from django.contrib import admin
from django.urls import path

from .views import index, index1, Index2

urlpatterns = [
    path('', index),
    path('func/', index1),
    path('class/', Index2.as_view())
]