from django.urls import path
from . import views

urlpatterns = [
    path('api/members/', views.add_member, name='add_member'),
]
