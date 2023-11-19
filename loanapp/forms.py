from django import forms 
from .models import ClientDetail, Collateral

class ClientDetailForm(forms.ModelForm):
    
    class Meta: 
        model= ClientDetail
        fields= '__all__' 
        
class CollateralForm(forms.ModelForm):
    class Meta:
        model= Collateral 
        fields= '__all__'        