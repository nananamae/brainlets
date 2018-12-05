from django.urls import path

from . import views

app_name = 'girlsfrontline'
urlpatterns = [
	path('', views.coming_soon, name='home'),
	path('batterycalculator/', views.battery_calculator, name='batterycalculator'),
	path('dailies/', views.coming_soon, name='dailies'),
]
