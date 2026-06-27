from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('offline/', views.offline, name='offline'),
    path('forms/contact.php', views.contact_submit, name='contact_submit'),
    path('forms/newsletter.php', views.newsletter_submit, name='newsletter_submit'),
]
