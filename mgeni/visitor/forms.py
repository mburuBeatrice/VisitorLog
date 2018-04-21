from django import forms
from .models import Visitor,County

class VisitorForm(forms.ModelForm):
    # gender = forms.ChoiceField(required=True, widget=forms.RadioSelect(
    # attrs={'class': 'Radio'}), choices=(('M','Male'),('F','Female')))
    arrival = forms.DateField(
    widget=forms.TextInput(     
        attrs={'type': 'date'} 
    )
)  
    departure = forms.DateField(
    widget=forms.TextInput(     
        attrs={'type': 'date'} 
    )
)
    class Meta:
        model = Visitor
        fields = ['name','gender'        
        ,'age','county','room','arrival','departure']
class CountyForm(forms.ModelForm):

    class Meta:
        model = County
        fields = ['name','code']
