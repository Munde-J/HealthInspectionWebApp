from django import forms
from .models import Business_type, Violation, Compliance, Inspection,InspectionChecklist,FollowUp
from django.forms import ModelForm
from .models import Business_type
from .models import Violation
from .models import Compliance
from .models import Inspection
from .models import InspectionChecklist
from .models import FollowUp



class Business_typeRegistrationForm(ModelForm):
    # meta class provides data for the class you're inheriting from'
  class Meta:
        model=Business_type
        fields=("name","address","city","country")
        widgets={
          "name":forms.TextInput(attrs={'class':'form-control','label':'name'}),
          "address":forms.TextInput(attrs={'class':'form-control','label':'address'}),
          "city":forms.TextInput(attrs={'class':'form-control','label':'city'}),
          "country":forms.TextInput(attrs={'class':'form-control','label':'country'}),     
        }

class ViolationRegistrationForm(ModelForm):
  class Meta:
        model=Violation
        fields=("business","date_time","violation_details","corrective_action") 
        widgets={
          "business":forms.TextInput(attrs={'class':'form-control','label':'business'}),
          "date_time":forms.TextInput(attrs={'class':'form-control','label':'date_time'}),     
          "violation_details":forms.TextInput(attrs={'class':'form-control','label':'violation_details'}),    
          "corrective_action":forms.TextInput(attrs={'class':'form-control','label':'corrective_action'}),
        }

class ComplianceRegistrationForm(ModelForm):
  class Meta:
        model=Compliance
        fields=("business","sanitation","water_quality","food_safety","disease_prevention")
        widgets={
          "business":forms.TextInput(attrs={'class':'form-control','label':'business'}),
          "sanitation":forms.TextInput(attrs={'class':'form-control','label':'sanitation'}),     
          "water_quality":forms.TextInput(attrs={'class':'form-control','label':'water_quality'}),    
          "food_safety":forms.TextInput(attrs={'class':'form-control','label':'food_safety'}),
          "disease_prevention":forms.TextInput(attrs={'class':'form-control','label':'disease_prevention'}),    
        }

class InspectionChecklistRegistrationForm(ModelForm):
  class Meta:
        model=InspectionChecklist
        fields=("business","cleanliness","protective_equipment","handwashing_equipment")
        widgets={
          "business":forms.TextInput(attrs={'class':'form-control','label':'business'}),
          "cleanliness":forms.TextInput(attrs={'class':'form-control','label':'cleanliness'}),
          "protective_equipment":forms.TextInput(attrs={'class':'form-control,','label':'protective_equipment'}),
          "handwashing_equipments":forms.TextInput(attrs={'class':'form-control','label':'handwashing_equipment'}),     
        }

class InspectionRegistrationForm(ModelForm):
  class Meta:
        model= Inspection
        fields=("business","date_time","observations")
        widgets={
          "business":forms.TextInput(attrs={'class':'form-control','label':'business'}),
          "observations":forms.TextInput(attrs={'class':'form-control','label':'business'}),
          "date_time":forms.TextInput(attrs={'class':'form-control','label':'business'}),
        }  

class FollowUpRegistrationForm(ModelForm):
  class Meta:
        model= FollowUp
        fields=("violation","date_time","followUp_details","followUp_status")
        widgets={
          "violation":forms.TextInput(attrs={'class':'form-control','label':'violation'}),
          "followUp_details":forms.TextInput(attrs={'class':'form-control','label':'followUp_details'}),
          "date_time":forms.TextInput(attrs={'class':'form-control','label':'date_time'}),
          "followUp_status":forms.TextInput(attrs={'class':'form-control','label':'followUp_status'}),
        }  
