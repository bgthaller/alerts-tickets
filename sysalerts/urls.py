from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'sysalerts'

urlpatterns = [
     path('', views.home, name='home'),
     path('alert_list', views.alert_list, name='alert_list'),
     path('edit/<int:id>/', views.edit_alert, name='edit_alert'),
     path('complete/<int:id>/', views.alt_complete, name='alt_complete'),
     path('history/', views.alert_history, name='alert_history'),
     path('view_tickets/', views.view_tickets, name='view_tickets'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
