from django.db import models
from pygments import lexers, highlight
from pygments.formatters import HtmlFormatter, ClassNotFound
from .utils import Preference as Pref
import time
# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    active = models.BooleanField(default=False)
    created_on = models.DateTimeField(null=True, blank=True)
    last_logged_in = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name + " : " + self.email
    class Meta:
        unique_together = (('name', 'email'),)


class Language(models.Model):
    name = models.CharField(max_length=100)
    lang_code = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    mime = models.CharField(max_length=100, help_text='MIME to use when sending snippet as file.')
    file_extension = models.CharField(max_length=10)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    def get_lexer(self):
        return lexers.get_lexer_by_name(self.lang_code)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('jobs:trending_snippets', args=[self.slug])

    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

class Snippet(models.Model):
    title = models.CharField(max_length=200, blank=True)
    original_code = models.TextField()
    highlighted_code = models.TextField()
    expiration = models.CharField(max_length=10, choices=Pref.expiration_choices)
    exposure = models.CharField(max_length=10, choices=Pref.exposure_choices)
    hits = models.IntegerField(default=0)
    slug = models.SlugField()
    created_on = models.DateTimeField(auto_now_add=True)

    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tag = models.ManyToManyField('Tag')

    class Meta:
        ordering = ['-created_on']

    def highlight(self):
        formatter = HtmlFormatter(linenos=True)
        return highlight(self.original_code, self.language.get_lexer(), formatter)

    def __str__(self):
        return (self.title if self.title else "Untitled") + " - " + self.language.name
    def get_absolute_url(self):

        return reverse('jobs:snippet_detail', args=[self.slug])
class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)

    def get_absolute_url(self):
        return reverse('jobs:tag_list', args=[self.slug])
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']
