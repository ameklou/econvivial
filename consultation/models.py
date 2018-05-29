from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# Create your models here.

class Consultation(models.Model):
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

    situation_choice=(
        ("Marie","Marie"),
        ("Divorce","Divorce"),
        ("Celibataire","Celibataire"),
        )

    owner=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="patient")
    created_at=models.DateField(auto_now_add=True)
    message=models.TextField()
    situation=models.CharField(max_length=250,choices=situation_choice)
    enfant=models.CharField(max_length=250,blank=True, null=True)
    motif=models.CharField(max_length=250,choices=motif_choice)
    ville=models.CharField(max_length=250,blank=True, null=True)
    voyage=models.CharField(max_length=250,choices=voyage_choice)
    slug=models.SlugField(max_length=250,blank=True, null=True)

    def __str__(self):
        return self.motif

    def get_absolute_url(self):
        return reverse('consultation_detail', args=[self.owner.pk,self.created_at.year,
                                                 self.created_at.strftime('%m'),
                                                 self.created_at.strftime('%d'),
                                                 self.slug])

class Answer(models.Model):
    consultation=models.ForeignKey(Consultation, on_delete=models.CASCADE)
    created_at=models.DateField(auto_now_add=True)
    answer=models.TextField()

    def __str__(self):
        return self.consultation.owner
