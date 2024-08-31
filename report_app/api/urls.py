from django.urls import path
from .views import reportCreate, reportList, reportDetail

urlpatterns = [
    path("create/", reportCreate.as_view(), name="report_create"),
    path("lists/", reportList.as_view(), name="report_lists"),
    path("details/<int:pk>/", reportDetail.as_view(), name="report_details")
]
