from django.db import models


class SponsorType(models.Model):
    name = models.CharField(max_length=32)


class Sponsor(models.Model):
    name = models.CharField(max_length=256)
    info = models.TextField(blank=True)
    logo = models.ImageField()
    sponsor_type = models.ForeignKey(
        SponsorType,
        on_delete=models.PROTECT,
    )
    sponsorship_date = models.DateField(null=True)
