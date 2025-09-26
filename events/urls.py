from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('services/', views.services_list, name='services'),
    path('services/<int:pk>/', views.service_detail, name='service_detail'),
    path('services/book/<int:pk>/', views.book_service, name='book_service'),
    path('packages/', views.packages_list, name='packages'),  # <-- added
    path('booking/success/', views.booking_success, name='booking_success'),
]
