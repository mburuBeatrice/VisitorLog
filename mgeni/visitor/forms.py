from django import forms
from .models import Visitor,County,Room,Availability

class VisitorForm(forms.ModelForm):
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
        ,'age','room','available','county','arrival','departure']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['available'].queryset = Availability.objects.none()

        if 'room' in self.data:
            try:
                room_type = int(self.data.get('room'))
                self.fields['available'].queryset = Availability.objects.filter(room_type=room_type).order_by('room_type')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['available'].queryset = self.instance.room.available_set.order_by('room_type')

class CountyForm(forms.ModelForm):

    class Meta:
        model = County
        fields = ['name','code']
