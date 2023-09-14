# appname/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.PersonListCreateView.as_view(), name='person-list-create'),
    path('api/<int:pk>', views.person_detail, name='person-detail'),
]