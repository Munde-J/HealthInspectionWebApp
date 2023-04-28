from django.contrib import admin

# Register your models here.
from .models import Business_type
from .models import Inspect
from .models import Compliance
from .models import InspectionChecklist
from .models import Violation
from .models import FollowUp

class Business_typeAdmin(admin.ModelAdmin):
    list_display = ('name','address','city','country',)
    search_fields = ('name','city',)
admin.site.register(Business_type,Business_typeAdmin)

class InspectAdmin(admin.ModelAdmin):
    list_display = ('business','date_time','observations',)
    search_fields = ('business','date_time',)
admin.site.register(Inspect,InspectAdmin)  

class ComplianceAdmin(admin.ModelAdmin):
    list_display = ('business','sanitation','water_quality','food_safety','disease_prevention',)
    search_fields = ('business','sanitation','water_quality',)
admin.site.register(Compliance,ComplianceAdmin)  

class InspectChecklistAdmin(admin.ModelAdmin):
    list_display = ('business','cleanliness','handwashing_equipment','protective_equipment',)
    search_fields = ('business','cleanliness','protective_equipment',)
admin.site.register(InspectionChecklist,InspectChecklistAdmin)  

class ViolationAdmin(admin.ModelAdmin):
    list_display = ('business','date_time','violation_details','corrective_action','observations',)
    search_fields = ('business','date_time',)
admin.site.register(Violation,ViolationAdmin)  

class FollowUpAdmin(admin.ModelAdmin):
    list_display = ('violation','date_time','followUp_details','followUp_status')
    search_fields = ('violation','date_time',)
admin.site.register(FollowUp,FollowUpAdmin)  

#inspector34-adminpassword



