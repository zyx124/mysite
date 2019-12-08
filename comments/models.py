from django.db import models
from django.utils import timezone
# Create your models here.


class Comment(models.Model):
    name = models.CharField('name', max_length=150)
    email = models.EmailField('email')
    url = models.TextField('url', blank=True)
    text = models.TextField('content')
    created_time = models.DateTimeField('created_time', default=timezone.now)
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return '{}: {}'.format(self.name, self.text[:20])
