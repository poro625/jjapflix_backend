from django.urls import path
from . import views

urlpatterns = [
    path('taste/', views.item_based_filtering, name='taste'),
    path('refresh/', views.MovieRefresh.as_view(), name='refresh'),

]