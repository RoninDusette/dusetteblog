from django.db import models
from django.template.defaultfilters import slugify
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from ckeditor_uploader.fields import RichTextUploadingField
import datetime


class Category(models.Model):
    name = models.CharField(max_length=200)
    photo = ProcessedImageField(format='JPEG', options={'quality': 60}, processors=[ResizeToFill(720, 510)], null=True, blank=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    category = models.ForeignKey(Category)
    date_added = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    body = RichTextUploadingField()
    photo = ProcessedImageField(format='JPEG', options={'quality': 60}, processors=[ResizeToFill(720, 510)])
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