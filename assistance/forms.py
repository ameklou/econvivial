from django import forms
from . models import Assistance, AssistanceAnser
from django_summernote.widgets import SummernoteWidget

class AssistanceForm(forms.ModelForm):
    class Meta:
        model = Assistance
        fields=['service','message']
        widgets={
        'message':SummernoteWidget(),
        }
class AnswerForm(forms.ModelForm):
    class Meta:
        model = AssistanceAnser
        fields=['message']
        widgets={
        'message':SummernoteWidget(),
        }
