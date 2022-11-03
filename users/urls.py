from django.urls import path
from users import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('signup/', views.UserView.as_view(), name='user_view'),
    path('api/token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
<<<<<<< HEAD
    path('<int:user_id>/', views.ProfileView.as_view(), name='profilw_view'),
    
=======
    path('<int:user_id>/', views.ProfileView.as_view(), name='profile_view'),
>>>>>>> 7f644ac28c4365267152dad5c1ad7a0b7e3c86ab
]