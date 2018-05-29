from django import forms
from . models import Assistance
from django_summernote.widgets import SummernoteWidget

class AssistanceForm(forms.ModelForm):
    class Meta:
        model = Assistance
        fields=['service','message']
        widgets={
        'message':SummernoteWidget(),
        }
