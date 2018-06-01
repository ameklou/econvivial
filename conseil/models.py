from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.conf import settings
from audiofield.fields import AudioField
import os.path

# Create your models here.
class PublishedManager(models.Manager):
      def get_queryset(self):
          return super(PublishedManager,
                        self).get_queryset()\
                             .filter(status='published')


class Post(models.Model):
    """
        Blog Posts
    """

    STATUS_CHOICES=(
        ('draft','Draft'),
        ('published','Published'),
    )
    title = models.CharField(max_length=250)
    cover=models.ImageField(upload_to="cover")
    #icon=models.ImageField(upload_to="icon", null=True, blank=True)
    body= models.TextField()
    slug= models.SlugField(max_length=250, unique_for_date="publish")
    author=models.ForeignKey(User, related_name="blog_posts")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    document=models.FileField(upload_to="document")
    audio_file = AudioField(upload_to='audios', blank=True,
                        ext_whitelist=(".mp3", ".wav", ".ogg"),
                        help_text=("Allowed type - .mp3, .wav, .ogg"))
    status = models.CharField(max_length=10,
                                 choices=STATUS_CHOICES,
                                 default='draft')

    #tags = TaggableManager()

    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    class Meta:
           ordering = ('-publish',)

    def __str__(self):
        return self.title

    def audio_file_player(self):
        """audio player tag for admin"""
        if self.audio_file:
            file_url = settings.MEDIA_URL + str(self.audio_file)
            #player_string = '<audio src="%s" controls>Your browser does not support the audio element.</audio>' % (file_url)
            return file_url
    audio_file_player.allow_tags = True
    audio_file_player.short_description = ('Audio file player')



    def get_absolute_url(self):
        return reverse('post_detail', args=[self.publish.year,
                                                 self.publish.strftime('%m'),
                                                 self.publish.strftime('%d'),
                                                 self.slug])
