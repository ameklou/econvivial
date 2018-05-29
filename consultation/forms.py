from django import forms
from . models import Consultation
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


# class ConsultationForm(forms.Form):
#     motif_choice=(
#           ("Ecoulement uretal","Ecoulement uretal"),
#           ("Ecoulement anaux","Ecoulement anaux"),
#           ("Douleurs anaux ou a la defacation","Douleurs anaux ou a la defacation"),
#           ("Pertes vaginales","Perte vaginales"),
#           ("Demangeaison","Demangeaison"),
#           ("Douleur a la miction","Douleur a la miction"),
#           ("Douleur lors des rapports sexuels","Douleur lors des rapports sexuels"),
#           ("Douleur au bas ventre","Douleur au bas ventre"),
#           ("Plaie genitale","Plaie genitale"),
#           ("Plaie anale","Plaie anale"),
#           ("Douleur et/ou Tumefaction du scrotum","Douleur et/ou Tumefaction du scrotum"),
#       )
#
#     voyage_choice=(
#       ("OUI","OUI"),
#       ("NON","NON"),
#       )
#     message=forms.CharField(widget=SummernoteWidget())
#     situation= forms.CharField()
#     nombre_enfant=forms.CharField()
#     motif=forms.ChoiceField(choices=motif_choice)
#     ville= forms.CharField()
#     voyage=forms.ChoiceField(choices=voyage_choice)


class ConsultationForm(forms.ModelForm):
    class Meta:
        model=Consultation
        fields=('motif','enfant','voyage','situation','ville','message')
        widgets={
        'message':SummernoteWidget(),
        }
