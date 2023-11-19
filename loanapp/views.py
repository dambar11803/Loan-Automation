from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import CreateView 
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .models import ClientDetail, Collateral
from .forms import ClientDetailForm, CollateralForm
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.


class homepage(TemplateView):
    template_name="base.html"
    
class AddClient(SuccessMessageMixin, CreateView):
    model= ClientDetail
    fields=['name','address','iro_address', 'iro_date','smi_address','smi_date','capital','capital_new',
            'pro_name','firm_type','exp_year','pre_sales','pre_networth','cur_sales','cur_sales','cur_networth'
            ,'business_type','product','product_types','brand','brand_types']   
    
    template_name='add_client.html' 
    success_url='/addclient/' 
    success_message="1 Client(s) added Successfully !!!"
    
class ClientList(ListView):
    model= ClientDetail
    template_name= 'client_list.html'      
    
#Display client details via DetailView    
class ClientDisplay(DetailView):
    model=ClientDetail
    template_name='client_display.html'
    
    
class ClientUpdate(UpdateView):
    model= ClientDetail 
    form_class= ClientDetailForm 
    template_name= 'client_update.html' 
    success_url= '/clientlist/'    

class ClientDelete(DeleteView):
    model= ClientDetail 
    template_name= 'client_delete.html'    
    success_url= '/clientlist/'
    

def CollateralDisplay(request):
    plot_no= plot_add= plot_owner=valuator= builidng_storey= ''
    distress_amt= mortgaged_amt= margin= building_value= total_amt= proposed_amt= old_margin= 0.0
    flag= None
    form= CollateralForm()
    if request.method=='POST':
        form= CollateralForm(request.POST)
        if form.is_valid():
            plot_no= form.cleaned_data['plot_no']
            plot_owner= form.cleaned_data['plot_owner']
            plot_add= form.cleaned_data['plot_add']
            valuator= form.cleaned_data['valuator']
            distress_amt= form.cleaned_data['distress_amt']
            margin= form.cleaned_data['margin']
            mortgaged_amt= form.cleaned_data['mortgaged_amt']
            building_value= form.cleaned_data['building_value']
            builidng_storey= form.cleaned_data['building_storey']
            
            if (building_value):
                total_amt= float(distress_amt) + float(building_value)
                temp= (100.0-margin)
                proposed_amt= ((total_amt*temp)/100)
                proposed_amt= round(proposed_amt,2)
                flag=True 
            elif (mortgaged_amt):
                total_amt= distress_amt
                old_margin= ((mortgaged_amt*100)/distress_amt)
                old_margin= round(old_margin,2)
                flag=False
            else:
                total_amt= distress_amt
                temp= (100.0-margin)
                proposed_amt= ((total_amt*temp)/100)
                proposed_amt= round(proposed_amt,2)
                flag=None
            
        else:
            form= CollateralForm()
    return render(request, 'collateral.html', {'form':form, 'plot_no':plot_no, 'plot_owner':plot_owner, 'plot_add':plot_add,
                                               'valuator':valuator, 'distress_amt':distress_amt, 'margin':margin,
                                               'mortgaged_amt':mortgaged_amt, 'building_value':building_value, 
                                               'building_storey':builidng_storey, 'total_amt':total_amt, 
                                               'proposed_amt':proposed_amt, 'flag':flag, 'old_margin':old_margin})            
        
        
        
    
    