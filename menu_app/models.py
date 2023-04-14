from django.db import models
from django.urls import reverse

class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200, blank=True, null=True)
    named_url = models.CharField(max_length=200, blank=True, null=True)
    menu_name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

    def get_url(self):
        if self.named_url:
            return reverse(self.named_url)
        return self.url
