from django.urls import path
from .views import budgetCreate, budgetList, budgetDetails

urlpatterns = [
    path("create/", budgetCreate.as_view(),name="budget_create"),
    path("lists/", budgetList.as_view(),name="budget_list"),
    path("details/<int:pk>/", budgetDetails.as_view(),name="budget")
]
