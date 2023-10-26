from django.urls import path
from DTP_map import views

app_name = 'DTP_map'
urlpatterns = [
    path('map/', views.mapbox_map, name='mapbox'),
]
