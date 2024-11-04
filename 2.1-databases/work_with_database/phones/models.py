from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    name = models.CharField(max_length=50, null=False)
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length =50)

    # TODO: Добавьте требуемые поля
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
