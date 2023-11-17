from django.contrib import admin
from . models import CrmContact,CrmCompany,CrmLead,JobApplication,EcommerceOrder,EcommerceCustomer,TicketList

# Register your models here.

@admin.register(CrmContact)
class CrmContactAdmin(admin.ModelAdmin):
    list_display = ['name','company_name','designation','email_id','phone','lead_score','tags','profile_pic']
    
@admin.register(CrmCompany)
class CrmCompanyAdmin(admin.ModelAdmin):
    list_display = ['name','owner_name','industry_type','rating','location','employee','website','contact_email','logo']
    
@admin.register(CrmLead)
class CrmLeadAdmin(admin.ModelAdmin):
    list_display = ['name','company_name','lead_score','phone','location','tags','profile_pic']
    
@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ['company_name','designation','apply_date','contact','type','status','profile_pic']
    
@admin.register(EcommerceOrder)
class EcommerceOrderAdmin(admin.ModelAdmin):
    list_display = ['name','product','order_date','amount','payment_method','status']
    
@admin.register(EcommerceCustomer)
class EcommerceCustomerAdmin(admin.ModelAdmin):
    list_display = ['name','email_id','phone','joining_date','status']
    
@admin.register(TicketList)
class TicketListAdmin(admin.ModelAdmin):
    list_display = ['title','client_name','assign_to','create_date','due_date','status','priority']
    
