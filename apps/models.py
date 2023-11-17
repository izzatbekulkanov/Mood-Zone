from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.

TAG_CHOICES = (
    ('Exiting','Exiting'),
    ('Lead','Lead'),
    ('Long-term','Long-term'),
    ('Partner','Partner'),
)

INDUSTRY_TYPE = (
    ('','Select industry type'),
    ('Computer Industry','Computer Industry'),
    ('Chemical Industries','Chemical Industries'),
    ('Health Services','Health Services'),
    ('Telecommunications Services','Telecommunications Services'),
    ('Textiles: Clothing, Footwear','Textiles: Clothing, Footwear')
)

STATUS_CHOICE = (
    ('Approved','Approved'),
    ('New','New'),
    ('Pending','Pending'),
    ('Rejected','Rejected')
)

TYPE_CHOICE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time')
)

STATUS = (
    ('Pending','Pending'),
    ('Inprogress','Inprogress'),
    ('Cancelled','Cancelled'),
    ('Pickups','Pickups'),
    ('Returns','Returns'),
    ('Delivered','Delivered')
)

PAYMENT_METHOD = (
    ('Mastercard','Mastercard'),
    ('Visa','Visa'),
    ('COD','COD'),
    ('Paypal','Paypal')
)

PRODUCT = (
    ('Puma Tshirt','Puma Tshirt'),
    ('Adidas Sneakers','Adidas Sneakers'),
    ('350 ml Glass Grocery Container','350 ml Glass Grocery Container'),
    ('American egale outfitters Shirt','American egale outfitters Shirt'),
    ('Galaxy Watch4','Galaxy Watch4'),
    ('Apple iPhone 12','Apple iPhone 12'),
    ('Funky Prints T-shirt','Funky Prints T-shirt'),
    ('USB Flash Drive Personalized with 3D Print','USB Flash Drive Personalized with 3D Print'),
    ('Oxford Button-Down Shirt','Oxford Button-Down Shirt'),
    ('Classic Short Sleeve Shirt','Classic Short Sleeve Shirt'),
    ('Half Sleeve T-Shirts (Blue)','Half Sleeve T-Shirts (Blue)'),
    ('Noise Evolve Smartwatch','Noise Evolve Smartwatch')
)

CUSTOMER_STATUS = (
    ('Active','Active'),
    ('Block','Block')
)

TICKET_STATUS = (
    ('Closed','Closed'),
    ('Inprogress','Inprogress'),
    ('New','New'),
    ('Open','Open')
)

PRIORITY = (
    ('High','High'),
    ('Low','Low'),
    ('Medium','Medium')
)

class CrmContact(models.Model):
    profile_pic = models.ImageField(upload_to="images/contact",blank=True,null=True)
    name = models.CharField(max_length=150)
    company_name = models.CharField(max_length=150)
    designation = models.CharField(max_length=150)
    email_id = models.EmailField(max_length=150,unique=True)
    phone = models.CharField(max_length=13)
    lead_score = models.IntegerField()
    tags = MultiSelectField(max_length=50,choices=TAG_CHOICES,max_choices=3)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def get_photo_url(self):
        if self.profile_pic and hasattr(self.profile_pic, 'url'):
            return self.profile_pic.url
        else:
            return "/static/images/users/user-dummy-img.jpg"
    
    
class CrmCompany(models.Model):
    logo = models.ImageField(upload_to='images/company',blank=True,null=True)
    name = models.CharField(max_length=150)
    owner_name = models.CharField(max_length=50)
    industry_type = models.CharField(max_length=50,choices=INDUSTRY_TYPE)
    rating = models.CharField(max_length=10)
    location = models.CharField(max_length=150)
    employee = models.CharField(max_length=10)
    website = models.CharField(max_length=150)
    contact_email = models.EmailField(max_length=150,unique=True)
    since = models.IntegerField()
    
    class Meta:
        verbose_name_plural = "Crm Companies"
        
    def get_photo_url(self):
        if self.logo and hasattr(self.logo, 'url'):
            return self.logo.url
        else:
            return "/static/images/users/multi-user.jpg"
    
class CrmLead(models.Model):
    profile_pic = models.ImageField(upload_to='images/leads',blank=True,null=True)
    name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=150)
    lead_score = models.IntegerField()
    phone = models.CharField(max_length=13)
    location = models.CharField(max_length=150)
    tags = MultiSelectField(max_length=50,choices=TAG_CHOICES,max_choices=3)
    create_date = models.DateField()
    
    def get_photo_url(self):
        if self.profile_pic and hasattr(self.profile_pic, 'url'):
            return self.profile_pic.url
        else:
            return "/static/images/users/user-dummy-img.jpg"
        
class JobApplication(models.Model):
    profile_pic = models.ImageField(upload_to='images/job/application',blank=True,null=True)
    company_name = models.CharField(max_length=150)
    designation = models.CharField(max_length=150)
    apply_date = models.DateField()
    contact = models.CharField(max_length=13)
    status = models.CharField(max_length=15,choices=STATUS_CHOICE)
    type = models.CharField(max_length=15,choices=TYPE_CHOICE)
    
class EcommerceOrder(models.Model):
    name = models.CharField(max_length=150)
    product = models.CharField(max_length=150,choices=PRODUCT)
    order_date = models.DateTimeField()
    amount = models.CharField(max_length=10)
    payment_method = models.CharField(max_length=50,choices=PAYMENT_METHOD)
    status = models.CharField(max_length=30,choices=STATUS)
    
class EcommerceCustomer(models.Model):
    name = models.CharField(max_length=50)
    email_id = models.EmailField(max_length=50,unique=True)
    phone = models.CharField(max_length=13)
    joining_date = models.DateField()
    status = models.CharField(max_length=12,choices=CUSTOMER_STATUS)
    
class TicketList(models.Model):
    title = models.CharField(max_length=150)
    client_name = models.CharField(max_length=100)
    assign_to = models.CharField(max_length=150)
    create_date = models.DateField()
    due_date = models.DateField()
    status = models.CharField(max_length=10,choices=TICKET_STATUS)
    priority = models.CharField(max_length=10,choices=PRIORITY)
    