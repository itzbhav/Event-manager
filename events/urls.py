from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),  # Root URL for homepage
    path('events/', views.event_list, name='event_list'),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
    path('events/create/', views.create_event, name='create_event'),
]
