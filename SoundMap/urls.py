from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('view/<int:map_id>/', views.show_map, name='show_map')
]