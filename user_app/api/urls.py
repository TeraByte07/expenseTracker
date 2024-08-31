from django.urls import path
from user_app.api.views import registration_view, logout_view
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', registration_view, name="register_account"),
    path('logout/', logout_view, name="logout_account"),
    path('login/', obtain_auth_token, name="login_account")
]
