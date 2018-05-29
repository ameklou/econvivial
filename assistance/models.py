from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Assistance(models.Model):

    service_choice=(
    ('Medecin','Medecin'),
    ('Gynecologue','Gynecologue'),
    ('Conseiller Psychosocial','Conseiller Psychosocial'),
    ('Sociologue','Sociologue'),
    ('Sage-femme','Sage-femme'),
    ('Pair-Educateur','Pair-Educateur'),
    )
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    service=models.CharField(max_length=250, choices=service_choice)
    message=models.TextField()
    slug=models.SlugField(max_length=250,blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.owner, self.service)

    def get_absolute_url(self):
        return reverse('assistance_detail', args=[self.owner
                                                self.created_at.year,
                                                 self.created_at.strftime('%m'),
                                                 self.created_at.strftime('%d'),
                                                 self.slug])
