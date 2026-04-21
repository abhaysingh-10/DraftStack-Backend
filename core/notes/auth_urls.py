from django.urls import path
from . import auth_views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView #JWT Auth

urlpatterns = [
    
    #OLD Token Auth 
    path('register/',auth_views.register ,name='register'),
    # path('login/',auth_views.login,name='login'),
    # path('logout/',auth_views.logout,name='logout'),
    
    # NEW JWT AUTH
    path('login/',TokenObtainPairView.as_view()),
    path('refresh/',TokenRefreshView.as_view()),
    path('logout/',auth_views.logout),    
    
]