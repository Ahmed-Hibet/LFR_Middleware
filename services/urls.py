from django.urls import path
from services.views import FacilityPendingList, LicenseRequest


urlpatterns = [
    path('facility/pending/', FacilityPendingList.as_view()),
    path('facility/license-request/<int:pk>/', LicenseRequest.as_view()),
]
