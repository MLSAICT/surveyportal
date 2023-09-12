from django import forms
from .models import ReferenceLetterPSM
from .models import RequestLetterPSM
from .models import PSMRequest
from .models import Islands

class ReferenceLetterPSMForm(forms.ModelForm):
    class Meta:
        model = ReferenceLetterPSM
        fields = ('document',)

class RequestLetterPSMForm(forms.ModelForm):
    class Meta:
        model = RequestLetterPSM
        fields = ('document1',)



class PSMRequestForm(forms.ModelForm):
    class Meta:
        model = PSMRequest
        fields = ('surveyor_name', 'island')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Retrieve the queryset for all islands ordered by name
        all_islands_by_name = Islands.objects.all().order_by('island_name')
        
        # Retrieve the queryset for all islands ordered by code
        all_islands_by_code = Islands.objects.all().order_by('island_code')

        # Update the choices for the island field
        self.fields['island'].queryset = all_islands_by_code