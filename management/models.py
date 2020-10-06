from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Asset(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    purchase_date = models.DateTimeField(blank=True, null=True)
    cost = models.FloatField(max_length=255)
    description = models.TextField(blank=True, null=True)
    asset_code = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Asset'

    def __str__(self):
        return '{}'.format(self.asset_code)


class Attachments(models.Model):
	attachment = models.FileField(upload_to='management', blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	belongs = models.ForeignKey(Asset, on_delete=models.CASCADE)



