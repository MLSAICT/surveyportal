from django import forms
from .models import RequestLetterPSM
from .models import PSMRequest
from .models import Islands
from .models import CSRRequest
from .models import CSRRequest


class CSRRequestForm(forms.ModelForm):
    class Meta:
        model = CSRRequest
        fields = ['surveyor_name', 'approved_psm', 'survey_report', 'csv_excel', 'raw_data']
        labels = {
            'surveyor_name': 'Surveyor Name',
            'approved_psm': 'Approved PSM Request',
            'survey_report': 'Survey Report',
            'csv_excel': 'CSV Excel',
            'raw_data': 'Raw Data',
        }


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

class CSRRequestForm(forms.ModelForm):
    class Meta:
        model = CSRRequest
        fields = {'surveyor_name','approved_psm'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Retrieve the queryset for all islands ordered by name
        all_islands_by_name = Islands.objects.all().order_by('island_name')
        
        # Retrieve the queryset for all islands ordered by code
        all_islands_by_code = Islands.objects.all().order_by('island_code')

        # Update the choices for the island field
        self.fields['island'].queryset = all_islands_by_code