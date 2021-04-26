from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('panel/', views.panel, name = 'panel'),
	path('delete/<int:email_id>/', views.delete, name = 'delete'),
	path('sendemail/', views.send_mails, name = 'sendemail'),
	path('info/', views.info, name = 'info')
]