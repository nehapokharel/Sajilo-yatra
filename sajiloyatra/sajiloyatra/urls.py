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
from django.contrib.auth import views as auth_views
from users import views as user_views
import django.contrib
from django.urls import path
from yatraapp import views

urlpatterns = [
    path('admin/', django.contrib.admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('home/', views.homeview, name='home'),
    path('food/', views.foodview, name='food'),
    path('food/category/',views.categoryview, name='category'),
    path('festival/', views.festivalview, name='festival'),
    path('events/',views.EventView.as_view(),name='event_list'),
    path('events/add/',views.EventCreateView.as_view(),name='event_create'),
    path('events/update/<int:pk>',views.EventUpdateView.as_view(),name= 'event_update'),
    path('events/completion/<int:pk>',views.eventcompletion ,name = 'event_completion'),
    path('contact/', views.contactview, name='contact'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
