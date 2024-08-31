from django.urls import path
from .views import recurringCreate

urlpatterns = [
    path("add/", recurringCreate.as_view(), name="add"),
]
