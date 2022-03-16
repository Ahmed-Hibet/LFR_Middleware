from django.urls import path
from check_list.views import (
    FacilityTypeList, FacilityTypeDetail, 
    LicenseRequirementList, LicenseRequirementDetail
    )

urlpatterns = [
    path('facility-type/', FacilityTypeList.as_view()),
    path('facility-type/<int:pk>/', FacilityTypeDetail.as_view()),
    path('license-requirement/', LicenseRequirementList.as_view()),
    path('license-requirement/<int:pk>/', LicenseRequirementDetail.as_view()),
]
