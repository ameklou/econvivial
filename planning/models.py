from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
# Create your models here.

class Planning(models.Model):
    title=models.CharField(max_length=256)
    cover=models.ImageField(upload_to='Planning')
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(max_length=256)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('plan_detail', args=[self.created_at.year,
                                                 self.created_at.strftime('%m'),
                                                 self.created_at.strftime('%d'),
                                                 self.slug])

class Consultation(models.Model):
    planning=models.ForeignKey(Planning)
    message=models.TextField()
    owner=models.ForeignKey(User, on_delete=models.CASCADE, related_name="plan_patient")
    created_at=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('plan_exchange',args=[self.created_at.year,
                                                self.created_at.strftime('%m'),
                                                self.created_at.strftime('%d'),
                                                self.owner.username])
class PlanAnswer(models.Model):
    consultation=models.ForeignKey(Consultation, on_delete=models.CASCADE, related_name="plan_patient_answer")
    answer=models.TextField()
    added_at=models.DateTimeField(auto_now_add=True)
    sender=models.ForeignKey(User, on_delete=models.CASCADE, related_name="plan_reponse")
