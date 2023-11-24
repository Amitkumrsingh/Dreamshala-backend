# yourapp/urls.py

from django.urls import path
from .views import UserCreateView, UserListCreateView, UserDetailView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('create/', UserCreateView.as_view(), name='user-create'),
]

# yourproject/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('dreamshala.urls')),
]

