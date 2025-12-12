from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Menu Items
    path('menu-items/', views.MenuItemsView.as_view()), # Changed to plural
    path('menu-items/<int:pk>/', views.SingleMenuItemView.as_view()), # Added trailing slash

    # Protected Message
    path('message/', views.msg),

    # Token Authentication
    path('api-token-auth/', obtain_auth_token),
]