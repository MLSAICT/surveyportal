from django import forms    
from user.models import PSMRequest  

class CommentForm(forms.ModelForm):
    class Meta:
        model = PSMRequest
        fields = ['comment']