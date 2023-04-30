from rest_framework import viewsets
from rest_framework import serializers

from healthapp.models import Business_type, Compliance, FollowUp, Inspection, InspectionChecklist, Violation
from.serializer import Business_typeSerializer, ComplianceSerializer, FollowUpSerializer, InspectSerializer, InspectionChecklistSerializer, ViolationSerializer



class Business_typeViewSet(viewsets.ModelViewSet):
    queryset = Business_type.objects.all()
    serializer_class = Business_typeSerializer
class InspectionViewSet(viewsets.ModelViewSet):
    queryset =Inspection.objects.all()
    serializer_class = InspectSerializer
class InspectionChecklistViewSet(viewsets.ModelViewSet):
    queryset=InspectionChecklist.objects.all()
    serializer_class= InspectionChecklistSerializer
class ViolationViewSet(viewsets.ModelViewSet):
    queryset=Violation.objects.all()
    serializer_class=ViolationSerializer
class ComplianceViewSet(viewsets.ModelViewSet):
    queryset=Compliance.objects.all()
    serializer_class=ComplianceSerializer
class FollowUpViewSet(viewsets.ModelViewSet):
    queryset=FollowUp.objects.all()
    serializer_class=FollowUpSerializer
