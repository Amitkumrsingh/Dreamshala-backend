# # api/urls.py
# from django.urls import path
# from .views import UserListCreateView, UserLogoutView
# from django.contrib import admin
# #urls.py
# from django.urls import path, include

# urlpatterns = [
#     path('', UserListCreateView.as_view(), name='user-signin'),
#     path('users/logout/', UserLogoutView.as_view(), name='user-logout'),
#     path('admin/', admin.site.urls),
#     path('api/', include('dreamshala.urls')),
# ]



# api/urls.py
from django.urls import path
from .views import UserListCreateView, UserLogoutView

urlpatterns = [
    path('users/signin/', UserListCreateView.as_view(), name='user-signin'),
    path('users/logout/', UserLogoutView.as_view(), name='user-logout'),
    # Add other URLs as needed
]
