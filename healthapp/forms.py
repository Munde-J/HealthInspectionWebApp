from django import forms
from .models import Currency, Customer, Notifications, Third_party
from django.forms import ModelForm
from .models import Business_type
from .models import Violation
from .models import Compliance
from .models import Inspect
from .models import InspectionChecklist
from .models import FollowUp



class Business_typeRegistrationForm(ModelForm):
    # meta class provides data for the class you're inheriting from'
  class Meta:
        model=Business_type
        fields=("name","address","city","country")
        widgets={
          "name":forms.TextInput(attrs={'class':'form-control'}),
          "address":forms.TextInput(attrs={'class':'form-control'}),
          "city":forms.TextInput(attrs={'class':'form-control'}),
          "country":forms.TextInput(attrs={'class':'form-control'}),     
        }

class ViolationRegistrationForm(ModelForm):
  class Meta:
        model=Violation
        fields=("business","date_time","violation_details","corrective_action") 
        widgets={
          "business":forms.TextInput(attrs={'class':'form-control'}),
          "date_time":forms.TextInput(attrs={'class':'form-control'}),     
          "violation_details":forms.TextInput(attrs={'class':'form-control'}),    
          "corrective_action":forms.TextInput(attrs={'class':'form-control'}),
        }

class ComplianceRegistrationForm(ModelForm):
  class Meta:
        model=Compliance
        fields=("business","sanitation","water_quality","food_safety","disease_prevention")
        widgets={
          "business":forms.TextInput(attrs={'class':'form-control'}),
          "sanitation":forms.TextInput(attrs={'class':'form-control'}),     
          "water_quality":forms.TextInput(attrs={'class':'form-control'}),    
          "food_safety":forms.TextInput(attrs={'class':'form-control'}),
          "disease_prevention":forms.TextInput(attrs={'class':'form-control'}),    
        }

class InspectionChecklistRegistrationForm(ModelForm):
  class Meta:
        model=InspectionChecklist
        fields=("business","cleanliness","protective_equipments","handwashing_equipments")
        widgets={
          "business":forms.TextInput(attrs={'class':'form-control'}),
          "cleanliness":forms.TextInput(attrs={'class':'form-control'}),
          "protective_equipments":forms.TextInput(attrs={'class':'form-control'}),
          "handwashing_equipments":forms.TextInput(attrs={'class':'form-control'}),     
        }

class InspectRegistrationForm(ModelForm):
  class Meta:
        model= Inspect
        fields=("business","date_time","observations")
        widgets={
          "business":forms.TextInput(attrs={'class':'form-control'}),
          "observations":forms.TextInput(attrs={'class':'form-control'}),
          "date_time":forms.TextInput(attrs={'class':'form-control'}),
        }  

class FollowUpRegistrationForm(ModelForm):
  class Meta:
        model= FollowUp
        fields=("violation","date_time","followUp_details","followUp_status")
        widgets={
          "violation":forms.TextInput(attrs={'class':'form-control'}),
          "followUp_details":forms.TextInput(attrs={'class':'form-control'}),
          "date_time":forms.TextInput(attrs={'class':'form-control'}),
          "followUp_status":forms.TextInput(attrs={'class':'form-control'}),
        }  
