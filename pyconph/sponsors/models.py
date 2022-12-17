from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.models import Orderable
from wagtail.snippets.models import register_snippet


class HomePageSponsorType(Orderable, models.Model):
    page = ParentalKey(
        "home.HomePage", on_delete=models.CASCADE, related_name="home_sponsor_type"
    )
    sponsor_type = models.ForeignKey(
        "sponsors.SponsorType",
        on_delete=models.CASCADE,
        related_name="sponsor_type_home",
    )


class HomePageSponsor(Orderable, models.Model):
    page = ParentalKey(
        "home.HomePage", on_delete=models.CASCADE, related_name="home_sponsor"
    )
    sponsor = models.ForeignKey(
        "sponsors.Sponsor", on_delete=models.CASCADE, related_name="sponsor_home"
    )


@register_snippet
class SponsorType(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


@register_snippet
class Sponsor(models.Model):
    name = models.CharField(max_length=256)
    info = models.TextField(blank=True)
    logo = models.ForeignKey(
        "wagtaildocs.Document",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    sponsor_type = models.ForeignKey(
        SponsorType,
        on_delete=models.PROTECT,
        related_name="sponsors",
    )
    website_url = models.URLField(blank=True, null=True)
    sponsorship_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name
