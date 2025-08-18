from django.urls import path
from . import views
from .views import (
    create_restaurant,
    list_restaurants,
    get_restaurant,
    update_restaurant,
    delete_restaurant
)

urlpatterns = [
    path('',views.homepage, name='homepage'),
    path('about/',views.about_us, name='about'),
    path('restaurants/', list_restaurants),
    path('restaurants/create/', create_restaurant),
    path('restaurants/<int:pk>/', get_restaurant),
    path('restaurants/<int:pk>/update/', update_restaurant),
    path('restaurants/<int:pk>/delete/', delete_restaurant),

]
