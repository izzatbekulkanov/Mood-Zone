from django import forms
from .models import CrmContact,CrmCompany,CrmLead,JobApplication,EcommerceOrder,EcommerceCustomer,TicketList

class CrmContactAddForm(forms.ModelForm):
    class Meta:
        model = CrmContact
        fields = ['profile_pic','name','company_name','designation','email_id','phone','lead_score','tags']
        
class CrmContactUpdateForm(forms.ModelForm):
    class Meta:
        model = CrmContact
        fields = ['profile_pic','name','company_name','designation','email_id','phone','lead_score','tags']
        
class CrmCompanyAddForm(forms.ModelForm):
    class Meta:
        model = CrmCompany
        fields = ['logo','name','owner_name','industry_type','rating','location','employee','website','contact_email','since']
        
class CrmCompanyUpdateForm(forms.ModelForm):
    class Meta:
        model = CrmCompany
        fields = ['logo','name','owner_name','industry_type','rating','location','employee','website','contact_email','since']
        
class CrmLeadsAddForm(forms.ModelForm):
    class Meta:
        model = CrmLead
        fields = ['profile_pic','name','company_name','lead_score','phone','location','tags','create_date']

class CrmLeadsUpdateForm(forms.ModelForm):
    class Meta:
        model = CrmLead
        fields = ['profile_pic','name','company_name','lead_score','phone','location','tags','create_date']
        
class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['profile_pic','company_name','designation','apply_date','contact','status','type']
        
class EcommerceOrderForm(forms.ModelForm):
    class Meta:
        model = EcommerceOrder
        fields = ['name','product','order_date','amount','payment_method','status']
        
class EcommerceCustomerForm(forms.ModelForm):
    class Meta:
        model = EcommerceCustomer
        fields = ['name','email_id','phone','joining_date','status']
        
class TicketListForm(forms.ModelForm):
    class Meta:
        model = TicketList
        fields = ['title','client_name','assign_to','create_date','due_date','status','priority']