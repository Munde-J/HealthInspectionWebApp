from rest_framework import serializers

from healthapp.models import (Business_type, Inspect, InspectionChecklist, Compliance, FollowUp,
                           Violation)

class Business_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business_type
        fields = ('name', 'address', 'city', 'country')
    
class InspectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inspect
        fields = ('business','date_time','observations')

class InspectionChecklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = InspectionChecklist
        fields = ('business','cleanliness','protective_equipments','handwashing_equipments')

class ComplianceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compliance
        fields = ('business','sanitation','water_quality','food_safety','disease_prevention')

class FollowUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowUp
        fields = ('violation','date_time','followUp_details','followUp_status')

class ViolationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Violation
        fields = ('business','date_time','observations','violation_details','corrective_actions')     
