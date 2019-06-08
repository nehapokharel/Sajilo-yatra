"""sajiloyatra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeview, name='home'),
    path('food/', views.foodview, name='food'),
    path('food/category/', views.categoryview, name='category'),
    path('festival/', views.festivalview, name='festival'),
    path('events/', views.EventView.as_view(), name='event_list'),
    path('events/completed/', views.EventCompleted.as_view(), name='event_list_completed'),
    path('events/add/', views.EventCreateView.as_view(), name='event_create'),
    path('events/update/<int:pk>', views.EventUpdateView.as_view(), name='event_update'),
    path('events/completion/<int:pk>', views.eventcompletion, name='event_completion'),
    path('contact/', views.contactview, name='contact'),
    path('thanks/',views.thankview, name='thanks'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
