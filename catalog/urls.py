from django.urls import path
from . import views


urlpatterns = [
 path('', views.index, name='index'),
 path(r'^dresss/$', views.DressListView.as_view(), name='Dresss'),
 path('dress/<int:pk>', views.DressDetailView.as_view(), name='dress-detail'),
 path(r'^guests/$', views.GuestListView.as_view(), name='Guests'),
 path('guest/<int:pk>', views.GuestDetailView.as_view(), name='guest-detail'),
]
