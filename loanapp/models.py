from django.db import models

# Create your models here.

FORM_CHOICES= [("Sole Prorprietorship", "Sole Proprietorship"),
               ("Private Limited", "Private Limited"),
               ("Corporation", "Corporation"),
               ("Partnership", "Partnership"),
               ("Limited Liability Company", "Limited Liability Company")]

class ClientDetail(models.Model):
    name= models.CharField(max_length=300)
    address= models.CharField(max_length=150)
    vdc= models.CharField(max_length=100, null=True, blank=True)
    vdc_date= models.CharField(max_length=12, null=True, blank=True)
    iro_address= models.CharField(max_length=50)
    iro_date= models.CharField(max_length=12)
    smi_address= models.CharField(max_length=50)
    smi_date= models.CharField(max_length=12)
    capital= models.CharField(max_length=20)
    capital_new= models.CharField(max_length=20, null=True, blank=True, default='') 
    
    # Firm Related 
    pro_name= models.CharField(max_length=100)
    firm_type= models.CharField(max_length=100, choices=FORM_CHOICES)
    exp_year= models.CharField(max_length=5, null=True, default='', blank=True)
    pre_sales= models.CharField(max_length=6, null=True, default='', blank=True)
    pre_networth= models.CharField(max_length=6, null=True, default='', blank=True)
    cur_sales= models.CharField(max_length=6, null=True, default='', blank=True)
    cur_networth= models.CharField(max_length=6, null=True, default='', blank=True)
    business_type= models.CharField(max_length=100, null=True, default='', blank=True)
    product= models.CharField(max_length=100, null=True, default='', blank=True)
    product_types= models.CharField(max_length=100, null=True, default='', blank=True)
    brand= models.CharField(max_length=100, default='', blank=True, null= True)
    brand_types= models.CharField(max_length=100, default='', blank=True, null=True)
   
    
    def __str__(self):
        return self.name 

class Collateral(models.Model):
    plot_no= models.CharField(max_length=30)
    plot_owner= models.CharField(max_length=100)
    plot_add= models.CharField(max_length=150)
    valuator= models.CharField(max_length=100)
    distress_amt= models.FloatField(max_length=50)
    margin= models.FloatField(max_length=50)
    mortgaged_amt= models.FloatField(max_length=50, null= True, blank= True)
    
    building_value= models.FloatField(max_length=5, null=True, blank= True)
    building_storey=models.CharField(max_length=10, null=True, blank= True)
    
    def __str__(self):
        return self.plot_owner 