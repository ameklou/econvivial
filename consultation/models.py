from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Consultation(models.Model):
    owner=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="patient")
    created_at=models.DateField(auto_now_add=True)
    message=models.TextField()
    situation=models.CharField(max_length=250,blank=True, null=True)
    enfant=models.CharField(max_length=250,blank=True, null=True)
    motif=models.CharField(max_length=250,blank=True, null=True)
    ville=models.CharField(max_length=250,blank=True, null=True)
    voyage=models.CharField(max_length=250,blank=True, null=True)
    slug=models.SlugField(max_length=250,blank=True, null=True)

    def __str__(self):
        return self.motif

    def get_absolute_url(self):
        return reverse('consultation_detail', args=[self.created_at.year,
                                                 self.created_at.strftime('%m'),
                                                 self.created_at.strftime('%d'),
                                                 self.slug])

class Answer(models.Model):
    consultation=models.ForeignKey(Consultation, on_delete=models.CASCADE)
    created_at=models.DateField(auto_now_add=True)
    answer=models.TextField()

    def __str__(self):
        return self.consultation.owner
