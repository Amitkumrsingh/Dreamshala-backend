from django.urls import path
from .views import UserCreateView, UserListCreateView, UserDetailView,ProfileAPIView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('create/', UserCreateView.as_view(), name='user-create'),
    path('api/accounts/profile/', ProfileAPIView.as_view(), name='profile-api')
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('dreamshala.urls')),
]



