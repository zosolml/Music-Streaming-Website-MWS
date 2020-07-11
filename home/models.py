from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class song_thumb(models.Model):
    artist=models.CharField(max_length=100,null=True)
    uploaded_by=models.CharField(max_length=100,null=True)
    song_title=models.CharField(max_length=100,null=True)
    slug=models.SlugField(max_length=250,null=True)
    album=models.CharField(max_length=100,null=True)
    song_duration=models.FloatField(null=True)
    img=models.ImageField(upload_to='pics',null=True)
    song=models.FileField(upload_to='media',null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('song_detail',args=[self.publish.year,
                             self.publish.month,
                             self.publish.day, self.slug])




    class Meta:
        ordering = ('-publish',)
    def __str__(self):
        return self.song_title

class Comment(models.Model):
    post = models.ForeignKey(song_thumb,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
