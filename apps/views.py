from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import CrmCompany,CrmContact,CrmLead,JobApplication,EcommerceOrder,EcommerceCustomer
from . forms import *
from django.contrib import messages

# Create your views here.
class AppsView(LoginRequiredMixin,TemplateView):
    pass

# Calendar
apps_calendar_view = AppsView.as_view(template_name="apps/apps-calendar.html")
# Chat
apps_chat_view = AppsView.as_view(template_name="apps/apps-chat.html")
# Mail Box
apps_mailbox_view = AppsView.as_view(template_name="apps/email/apps-mailbox.html")
apps_basicaction_view = AppsView.as_view(template_name="apps/email/apps-email-basic.html")
apps_invoiceaction_view = AppsView.as_view(template_name="apps/email/apps-email-ecommerce.html")

# Ecommerce
apps_ecommerce_products_view = AppsView.as_view(template_name="apps/ecommerce/apps-ecommerce-products.html")
apps_ecommerce_product_details_view = AppsView.as_view(template_name="apps/ecommerce/apps-ecommerce-product-details.html")
apps_ecommerce_add_product_view = AppsView.as_view(template_name="apps/ecommerce/apps-ecommerce-add-product.html")
# apps_ecommerce_orders_view = AppsView.as_view(template_name="apps/ecommerce/apps-ecommerce-orders.html")
apps_ecommerce_order_details_view = AppsView.as_view(template_name="apps/ecommerce/apps-ecommerce-order-details.html")
# apps_ecommerce_customers_view = AppsView.as_view(template_name="apps/ecommerce/apps-ecommerce-customers.html")
apps_ecommerce_cart_view = AppsView.as_view(template_name="apps/ecommerce/apps-ecommerce-cart.html")
apps_ecommerce_checkout_view = AppsView.as_view(template_name="apps/ecommerce/apps-ecommerce-checkout.html")
apps_ecommerce_sellers_view = AppsView.as_view(template_name="apps/ecommerce/apps-ecommerce-sellers.html")
apps_ecommerce_seller_details_view = AppsView.as_view(template_name="apps/ecommerce/apps-ecommerce-seller-details.html")

# Projects
apps_projects_list_view = AppsView.as_view(template_name="apps/projects/apps-projects-list.html")
apps_projects_overview_view = AppsView.as_view(template_name="apps/projects/apps-projects-overview.html")
apps_projects_create_view = AppsView.as_view(template_name="apps/projects/apps-projects-create.html")

# Tasks
apps_tasks_kanban_view = AppsView.as_view(template_name="apps/tasks/apps-tasks-kanban.html")
apps_tasks_list_view = AppsView.as_view(template_name="apps/tasks/apps-tasks-list-view.html")
apps_tasks_details_view = AppsView.as_view(template_name="apps/tasks/apps-tasks-details.html")

# CRM
# apps_crm_contacts_view = AppsView.as_view(template_name="apps/crm/apps-crm-contacts.html")
# apps_crm_companies_view = AppsView.as_view(template_name="apps/crm/apps-crm-companies.html")
apps_crm_deals_view = AppsView.as_view(template_name="apps/crm/apps-crm-deals.html")
# apps_crm_leads_view = AppsView.as_view(template_name="apps/crm/apps-crm-leads.html")

# Crypto
apps_crypto_transactions_view = AppsView.as_view(template_name="apps/crypto/apps-crypto-transactions.html")
apps_crypto_buy_sell_view = AppsView.as_view(template_name="apps/crypto/apps-crypto-buy-sell.html")
apps_crypto_orders_view = AppsView.as_view(template_name="apps/crypto/apps-crypto-orders.html")
apps_crypto_wallet_view = AppsView.as_view(template_name="apps/crypto/apps-crypto-wallet.html")
apps_crypto_ico_view = AppsView.as_view(template_name="apps/crypto/apps-crypto-ico.html")
apps_crypto_kyc_view = AppsView.as_view(template_name="apps/crypto/apps-crypto-kyc.html")

# Invoices
apps_invoices_list_view = AppsView.as_view(template_name="apps/invoices/apps-invoices-list.html")
apps_invoices_details_view = AppsView.as_view(template_name="apps/invoices/apps-invoices-details.html")
apps_invoices_create_view = AppsView.as_view(template_name="apps/invoices/apps-invoices-create.html")

# Support Tickets
# apps_tickets_list_view = AppsView.as_view(template_name="apps/support-tickets/apps-tickets-list.html")
apps_tickets_details_view = AppsView.as_view(template_name="apps/support-tickets/apps-tickets-details.html")

#NFT pages
apps_nft_marketplace_view = AppsView.as_view(template_name="apps/nft/apps-nft-marketplace.html")
apps_nft_explore_view = AppsView.as_view(template_name="apps/nft/apps-nft-explore.html")
apps_nft_liveauction_view = AppsView.as_view(template_name="apps/nft/apps-nft-auction.html")
apps_nft_itemdetails_view= AppsView.as_view(template_name="apps/nft/apps-nft-item-details.html")
apps_nft_collections_view= AppsView.as_view(template_name="apps/nft/apps-nft-collections.html")
apps_nft_creators_view = AppsView.as_view(template_name="apps/nft/apps-nft-creators.html")
apps_nft_ranking_view = AppsView.as_view(template_name="apps/nft/apps-nft-ranking.html")
apps_nft_wallet_view = AppsView.as_view(template_name="apps/nft/apps-nft-wallet.html")
apps_nft_create_view = AppsView.as_view(template_name="apps/nft/apps-nft-create.html")

#Job Pages
# apps_job_application_view = AppsView.as_view(template_name="apps/job/apps-job-application.html")
apps_job_candidate_grid_view = AppsView.as_view(template_name="apps/job/apps-job-candidate-grid.html")
apps_job_candidate_lists_view = AppsView.as_view(template_name="apps/job/apps-job-candidate-lists.html")
apps_job_categories_view = AppsView.as_view(template_name="apps/job/apps-job-categories.html")
apps_job_companies_list_view = AppsView.as_view(template_name="apps/job/apps-job-companies-lists.html")
apps_job_details_view = AppsView.as_view(template_name="apps/job/apps-job-details.html")
apps_job_grid_lists_view = AppsView.as_view(template_name="apps/job/apps-job-grid-lists.html")
apps_job_lists_view = AppsView.as_view(template_name="apps/job/apps-job-lists.html")
apps_job_new_view = AppsView.as_view(template_name="apps/job/apps-job-new.html")
apps_job_statistics_view = AppsView.as_view(template_name="apps/job/apps-job-statistics.html")

# Calendar
apps_file_manager_view = AppsView.as_view(template_name="apps/apps-file-manager.html")

# Calendar
apps_todo_view = AppsView.as_view(template_name="apps/apps-todo.html")
apps_api_key_view = AppsView.as_view(template_name="apps/apps-api-key.html")

# Crm Contact views
def apps_crm_contacts_view(request,pk):
    contacts = CrmContact.objects.all().order_by('-id')
    if contacts:
        contact = CrmContact.objects.get(pk=pk)
    return render(request,"apps/crm/apps-crm-contacts.html",{'contacts':contacts,'contact':contact})

def apps_crm_add_contacts_view(request):
    contacts = CrmContact.objects.all().order_by("-id")
    
    if request.method == 'POST':
        form = CrmContactAddForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,"Contact inserted successfully!")
            return redirect("apps:crm.contacts")
        else:
            messages.error(request,"Something went wrong!")
            return redirect("apps:crm.contacts")
    return render(request,"apps/crm/apps-crm-contacts.html",{'contacts':contacts})

def apps_crm_update_contacts_view(request,pk):
    contacts = CrmContact.objects.get(pk=pk)
    if request.method == "POST":
        form = CrmContactUpdateForm(request.POST or None,request.FILES or None,instance=contacts)
        if form.is_valid():
            form.save()
            messages.success(request,"Contact updated successfully!")
            return redirect("apps:crm.contacts")
        else:
            messages.error(request,"Something went wrong!")
            return redirect("apps:crm.contacts")
    return render(request,'apps/crm/apps-crm-contacts.html')

def apps_crm_delete_contacts_view(request,pk):
    contacts = CrmContact.objects.get(pk=pk)
    contacts.delete()
    messages.success(request,"Contact deleted successfully!")
    return redirect("apps:crm.contacts")

# Crm Companies views

def apps_crm_companies_view(request,pk):
    companies = CrmCompany.objects.all().order_by('-id')
    if companies:
        company = CrmCompany.objects.get(pk=pk)
    return render(request,"apps/crm/apps-crm-companies.html",{'companies':companies,'company':company})

def apps_crm_add_companies_view(request):
    companies = CrmCompany.objects.all().order_by('-id')
    if request.method == "POST":
        form = CrmCompanyAddForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,"Company inserted successfully!")
            return redirect("apps:crm.companies")
        else:
            messages.error(request,"Something went wrong!")
            return redirect("apps:crm.companies")
    return render(request,"apps/crm/apps-crm-companies.html",{'companies':companies})

def apps_crm_update_companies_view(request,pk):
    companies = CrmCompany.objects.get(pk=pk)
    if request.method == "POST":
        form = CrmCompanyUpdateForm(request.POST or None,request.FILES or None,instance=companies)
        if form.is_valid():
            form.save()
            messages.success(request,"Company updated successfully!")
            return redirect("apps:crm.companies")
        else:
            messages.error(request,"Something went wrong!")
            return redirect("apps:crm.companies")
    return render(request,"apps/crm/apps-crm-companies.html")

def apps_crm_delete_companies_view(request,pk):
    companies = CrmCompany.objects.get(pk=pk)
    companies.delete()
    messages.success(request,"Contact deleted successfully!")
    return redirect("apps:crm.companies")

# Crm Leads views

def apps_crm_leads_view(request):
    leads = CrmLead.objects.all().order_by('-id')
    if request.method == 'POST':
        form = CrmLeadsAddForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,"Lead inserted successfully!")
            return redirect("apps:crm.leads")
        else:
            messages.error(request,"Something went wrong!")
            return redirect("apps:crm.leads")
    return render(request,"apps/crm/apps-crm-leads.html",{'leads':leads})

def apps_crm_update_leads_view(request,pk):
    leads = CrmLead.objects.get(pk=pk)
    if request.method == "POST":
        form = CrmLeadsUpdateForm(request.POST or None,request.FILES or None,instance=leads)
        if form.is_valid():
            form.save()
            messages.success(request,"Lead Updated successfully!")
            return redirect("apps:crm.leads")
        else:
            messages.error(request,"Something went wrong!")
            return redirect("apps:crm.leads")
    return render(request,"apps/crm/apps-crm-leads.html")

def apps_crm_delete_leads_view(request,pk):
    leads = CrmLead.objects.get(pk=pk)
    leads.delete()
    messages.success(request,"Contact deleted successfully!")
    return redirect("apps:crm.leads")

def apps_job_application_view(request):
    apps = JobApplication.objects.all().order_by('-id')
    if request.method == "POST":
        form = JobApplicationForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,'Application inserted Successfully!')
            return redirect("apps:job.application")
        else:
            messages.error(request,'Something went wrong!')
            return redirect('apps:job.application')
    return render(request,"apps/job/apps-job-application.html",{'apps':apps})

def apps_job_update_application_view(request,pk):
    apps = JobApplication.objects.get(pk=pk)
    if request.method == "POST":
        form = JobApplicationForm(request.POST or None, request.FILES or None, instance=apps)
        if form.is_valid():
            form.save()
            messages.success(request,'Application updated Successfully!')
            return redirect('apps:job.application')
        else:
            messages.error(request,'Something went wrong!')
            return redirect('apps:job.application')
    return render(request,'apps/jobs/apps-job-application.html')

def apps_job_delete_application_view(request,pk):
    apps = JobApplication.objects.get(pk=pk)
    apps.delete()
    messages.success(request,'Application deleted Successfully!')
    return redirect("apps:job.application")

def apps_ecommerce_orders_view(request):
    orders = EcommerceOrder.objects.all().order_by('-id')
    if request.method == "POST":
        form = EcommerceOrderForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,'Order inserted Successfully!')
            return redirect('apps:ecommerce.orders')
        else:
            messages.error(request,'Something went wrong!')
            return redirect('apps:ecommerce.orders')
    return render(request,'apps/ecommerce/apps-ecommerce-orders.html',{'orders':orders})

def apps_ecommerce_update_orders_view(request,pk):
    orders = EcommerceOrder.objects.get(pk=pk)
    if request.method == "POST":
        form = EcommerceOrderForm(request.POST or None,request.FILES or None,instance=orders)
        if form.is_valid():
            form.save()
            messages.success(request,'Order updated Successfully!')
            return redirect('apps:ecommerce.orders')
        else:
            messages.error(request,'Something went wrong!')
            return redirect('apps:ecommerce.orders')
    return render(request,'apps/ecommerce/apps-ecommerce-orders.html')

def apps_ecommerce_delete_orders_view(request,pk):
    orders = EcommerceOrder.objects.get(pk=pk)
    orders.delete()
    messages.success(request,'Order deleted Successfully!')
    return redirect('apps:ecommerce.orders')

def apps_ecommerce_customers_view(request):
    customers = EcommerceCustomer.objects.all().order_by('-id')
    if request.method == "POST":
        form = EcommerceCustomerForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,'Customer inserted Successfully!')
            return redirect('apps:ecommerce.customers')
        else:
            messages.error(request,'Something went wrong!')
            return redirect('apps:ecommerce.customers')
    return render(request,'apps/ecommerce/apps-ecommerce-customers.html',{'customers':customers})

def apps_ecommerce_update_customers_view(request,pk):
    customers = EcommerceCustomer.objects.get(pk=pk)
    if request.method == "POST":
        form = EcommerceCustomerForm(request.POST or None,request.FILES or None,instance=customers)
        if form.is_valid():
            form.save()
            messages.success(request,'Customer updated Successfully!')
            return redirect('apps:ecommerce.customers')
        else:
            messages.error(request,'Something went wrong!')
            return redirect('apps:ecommerce.customers')
    return render(request,'apps/ecommerce/apps-ecommerce-customers.html')

def apps_ecommerce_delete_customers_view(request,pk):
    customers = EcommerceCustomer.objects.get(pk=pk)
    customers.delete()
    messages.success(request,'Customer deleted Successfully!')
    return redirect('apps:ecommerce.customers')

def apps_tickets_list_view(request):
    tickets = TicketList.objects.all().order_by('-id')
    if request.method == "POST":
        form = TicketListForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,'Ticket inserted Successfully!')
            return redirect('apps:tickets.list')
        else:
            messages.error(request,'Something went wrong!')
            return redirect('apps:tickets.list')
    return render(request,'apps/support-tickets/apps-tickets-list.html',{'tickets':tickets})

def apps_tickets_update_list_view(request,pk):
    tickets = TicketList.objects.get(pk=pk)
    if request.method == "POST":
        form = TicketListForm(request.POST or None,request.FILES or None,instance=tickets)
        if form.is_valid():
            form.save()
            messages.success(request,'Ticket updated Successfully!')
            return redirect('apps:tickets.list')
        else:
            messages.error(request,'Something went wrong!')
            return redirect('apps:tickets.list')
    return render(request,'apps/support-tickets/apps-tickets-list.html')

def apps_tickets_delete_list_view(request,pk):
    tickets = TicketList.objects.get(pk=pk)
    tickets.delete()
    messages.success(request,'Ticket deleted Successfully!')
    return redirect('apps:tickets.list')
    