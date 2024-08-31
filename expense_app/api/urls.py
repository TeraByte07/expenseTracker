from django.urls import path
from .views import expenseCreate, expenseList, expenseDetails#, expenseAnalysis

urlpatterns = [
    path("create/", expenseCreate.as_view(), name="expense_create"),
    path("lists/", expenseList.as_view(), name="expense_lists"),
    path("details/<int:pk>/", expenseDetails.as_view(), name="expense_details"),
    #path("analysis/", expenseAnalysis.as_view(), name="expense_analysis"),
]
