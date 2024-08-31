from django.urls import path
from .views import incomeCreate, incomeList, incomeDetails

urlpatterns = [
    path("create/", incomeCreate.as_view(),name="income_create"),
    path("lists/", incomeList.as_view(),name="income_list"),
    path("details/<int:pk>/", incomeDetails.as_view(),name="income")
]
