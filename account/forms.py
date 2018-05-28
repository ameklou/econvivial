from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class SignUpForm(UserCreationForm):
    sexe_choice=(
    ("M","MASCULIN"),
    ("F","FEMININ"),

    )

    region_choice=(
    ("Lome commune","Lome commune"),
    ("Maritime","Maritime"),
    ("Plateau","Plateau"),
    ("Centrale","Centrale"),
    ("kara","Kara"),
    ("Savane","Savane"),

    )

    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    phone= forms.CharField()
    phone= forms.CharField()
    sexe= forms.CharField()
    profession= forms.CharField()
    region=forms.ChoiceField(choices=region_choice)


    class Meta:
        model = User
        fields = ('username','email', 'birth_date', 'password1', 'profession' ,'phone','birth_date','region','sexe' )
        #widgets = {'country': CountrySelectWidget()}

class SigninForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())


class ConsultationForm(forms.Form):
    motif_choice=(
          ("Ecoulement uretal","Ecoulement uretal"),
          ("Ecoulement anaux","Ecoulement anaux"),
          ("Douleurs anaux ou a la defacation","Douleurs anaux ou a la defacation"),
          ("Pertes vaginales","Perte vaginales"),
          ("Demangeaison","Demangeaison"),
          ("Douleur a la miction","Douleur a la miction"),
          ("Douleur lors des rapports sexuels","Douleur lors des rapports sexuels"),
          ("Douleur au bas ventre","Douleur au bas ventre"),
          ("Plaie genitale","Plaie genitale"),
          ("Plaie anale","Plaie anale"),
          ("Douleur et/ou Tumefaction du scrotum","Douleur et/ou Tumefaction du scrotum"),
      )

    voyage_choice=(
      ("OUI","OUI"),
      ("NON","NON"),
      )
    message=forms.CharField(widget=SummernoteWidget())
    situation= forms.CharField()
    nombre_enfant=forms.CharField()
    motif=forms.ChoiceField(choices=motif_choice)
    ville= forms.CharField()
    voyage=forms.ChoiceField(choices=voyage_choice)
