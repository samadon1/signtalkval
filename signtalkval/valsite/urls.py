from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('main/<int:pk>/', views.main, name='main'),
    path('is_correct/<int:pk>/', views.is_correct, name='is_correct'),
    path('update_text/<int:pk>/<int:page>/', views.update_text, name='update_text'),

]