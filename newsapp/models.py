from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='post_photo', null=True)
    date_created = models.DateTimeField(default=timezone.now, blank=True)
    author = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="news")
    count = models.PositiveIntegerField(default=1, null=True, blank=True)

    def __str__(self):
        return self.author

    # def update_counter(self):
    #     if self.count is not None:
    #         self.count += 1
    #     else:
    #         self.count = 0

    class Meta:
        ordering = ['-id']


class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'
