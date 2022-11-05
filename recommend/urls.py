from django.urls import path
from . import views

urlpatterns = [
    path('refresh/', views.MovieRefresh.as_view(), name='refresh'),
    path('<str:movie_title>/', views.TasteView.as_view(), name='taste'),

]