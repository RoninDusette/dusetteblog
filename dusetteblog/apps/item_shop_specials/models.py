from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class ItemShopSpecials(models.Model):
    name = models.CharField(max_length=200)
    photo = ProcessedImageField(format='JPEG', options={'quality': 60}, processors=[ResizeToFill(720, 650)], null=True, blank=True)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    description = models.CharField(max_length=200)
    item_url = models.URLField()
    price = models.FloatField()
    discount = models.FloatField()
    slug = models.SlugField(blank=True, editable=False)

    def __str__(self):
        return self.name