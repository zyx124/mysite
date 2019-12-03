from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.html import strip_tags
from django.urls import reverse
import markdown

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()

    created_time = models.DateTimeField(default=timezone.now)
    modified_time = models.DateTimeField()

    # the abstract of the article, empty value allowable.
    excerpt = models.CharField(max_length=200, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()

        md = markdown.Markdown(extensions=['markdown.extensions.extra',
                                           'markdown.extensions.codehilite',])

        # take the first 54 words to automatically generate the excerpt
        # strip_tags is used to exclude the HTML tags.
        self.excerpt = strip_tags(md.convert(self.body))[:554]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    #self defined url getting method
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})