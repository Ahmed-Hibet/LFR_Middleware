from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from check_list.models import FacilityType, LicenseRequirement
import requests


class FacilityPendingList(APIView):
    """
    Listing all pending facilities
    """
    def get(self, request, format=None):
        url = "http://127.0.0.1:1000/api/facility/"
        facility_list_object = requests.get(url)

        if facility_list_object.status_code != 200:
            return Response(facility_list_object.status_code)
        facility_list = facility_list_object.json()
        pending_facility_list = []
        for facility in facility_list:
            if facility['status'] == 'Pending':
                pending_facility_list.append(facility)
        return Response(pending_facility_list, status=status.HTTP_200_OK)


class LicenseRequest(APIView):
    """
    Apply for license
    """

    def compare_againest_checklist(self, data, *args, **kwargs):
        facility_type = data['facility_types'][0]
        check_list_type = FacilityType.objects.filter(facility_type_name=facility_type).first()
        check_list = LicenseRequirement.objects.filter(facility_type=check_list_type)

        for requirement in check_list:
            name = requirement.requirement_name
            value = requirement.required_value
            # print(data[name], value)
            if name not in data:
                return False
            if data[name] < value:
                return False
        return True

    def get(self, request, pk, fromat=None):
        url = "http://127.0.0.1:1000/api/facility/" + str(pk) + '/'
        facility_object = requests.get(url)

        if facility_object.status_code != 200:
            return Response(facility_object.status_code)
        facility = facility_object.json()
        return Response(facility, status=status.HTTP_200_OK)

    def put(self, request, pk, formate=None):
        self.data = request.data
        if not self.compare_againest_checklist(self.data):
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        url = "http://127.0.0.1:1000/api/facility/" + str(pk) + '/'
        self.data['status'] = 'Approved'
        facility_object = requests.put(url, data=self.data)
        if facility_object.status_code != 200:
            return Response(status=facility_object.status_code)
        return Response(facility_object.json(), status=status.HTTP_200_OK)
