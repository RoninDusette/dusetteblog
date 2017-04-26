from django.db import models
from django.template.defaultfilters import slugify
from ckeditor_uploader.fields import RichTextUploadingField
import datetime


class Article(models.Model):
    CATEGORY_CHOICES = (
        ('General', 'General'),
        ('Photography', 'Photography'),
        ('Tech', 'Tech'),
    )
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES)
    date_added = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    body = RichTextUploadingField()
    photo = models.ImageField()
    slug = models.SlugField(unique=True, blank=True, editable=False)

    def __str__(self):
        return self.title

    def save(self):
        super(Article, self).save()
        date = datetime.datetime.today()
        self.slug = '%i/%i/%i/%i-%s' % (
            date.year, date.month, date.day, self.id, slugify(self.title)
        )
        super(Article, self).save()