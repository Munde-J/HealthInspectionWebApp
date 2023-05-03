from django .urls import path
# from healthapp.models import Business_type
from .views import register_business_type
from .views import register_violation
from .views import register_compliance
from .views import register_inspection
from .views import register_inspectionChecklist
from .views import register_followUp



app_name = "healthapp"

urlpatterns = [
    path("business_type/", register_business_type, name = "registration"),
    

    path("followUp/", register_followUp, name = "registration"),
    
    path("inspection/", register_inspection, name = "registration"),
    
    path("inspectionChecklist/", register_inspectionChecklist, name = "registration"),
    
    path("violation/", register_violation, name = "registration"),
    

    path("compliance/", register_compliance, name = "registration"),
    

]