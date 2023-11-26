"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path

from core import settings
from danielAgency.views import *

urlpatterns = [
    path('accounts/login/', SubmittableLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-change/', SubmittablePasswordChangeView.as_view(),
         name='password_change'),
    path('sign-up/', SignUpView.as_view(), name='sign_up'),
    path('admin/', admin.site.urls),
    path('list/', TripListView.as_view(), name='list'),
    path('trip/create_form', TripCreateView.as_view(), name='trip_create_form'),
    path('trip/update/<pk>', TripUpdateView.as_view(), name='trip_update'),
    path('trip/delete/<pk>', TripDeleteView.as_view(), name='trip_delete'),
    path('', TripCardView.as_view(), name='trip'),
    path('trip/<pk>/', TripDetailView.as_view(), name='trip_detail'),
    path('book_now/<int:pk>/', book_now, name='book_now'),
    path('watch/<pk>', WatchTour.as_view(), name='tour_watch'),
    path('about_us/', about_us, name='about_us'),
    path('contact/', contact_us, name='contact_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
