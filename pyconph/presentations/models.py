from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Orderable
from wagtail.snippets.models import register_snippet


class SpeakerHomeRelationship(Orderable, models.Model):
    page = ParentalKey(
        "home.HomePage",
        related_name="home_speaker",
        on_delete=models.CASCADE,
    )
    speaker = models.ForeignKey(
        "presentations.Speaker",
        related_name="speaker_home",
        on_delete=models.CASCADE,
    )
    panels = [FieldPanel("speaker")]


class KeynoteSpeakerHomeRelationship(Orderable, models.Model):
    page = ParentalKey(
        "home.HomePage",
        related_name="home_keynotespeaker",
        on_delete=models.CASCADE,
    )
    speaker = models.ForeignKey(
        "presentations.Speaker",
        related_name="keynotespeaker_home",
        on_delete=models.CASCADE,
    )
    panels = [FieldPanel("speaker")]


@register_snippet
class Speaker(Orderable, models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64, blank=True)
    title = models.CharField(
        max_length=128,
        blank=True,
        help_text="Short title to call the speaker, eg: CEO of X company",
    )
    display_photo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    introduction = models.TextField(blank=True)
    is_featured = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Schedule(Orderable, models.Model):
    class Days(models.TextChoices):
        DAY1 = ("day1", "1st Day")
        DAY2 = ("day2", "2nd Day")

    page = ParentalKey(
        "home.HomePage", related_name="schedules", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    description = RichTextField(blank=True)
    location = models.CharField(max_length=255)

    day = models.CharField(
        choices=Days.choices,
        max_length=16,
    )
    time_start = models.TimeField()
    time_end = models.TimeField()

    speaker = models.ForeignKey(
        Speaker,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    @property
    def time(self):
        fmt = "%-I:%M %p"
        start = self.time_start.strftime(fmt)
        end = self.time_end.strftime(fmt)
        return f"{start} - {end}"


class Presentation(models.Model):
    class PresentationTypes(models.TextChoices):
        TALK = ("talk", "Talk")
        WORKSHOP = ("workshop", "Workshop")
        PANEL = ("panel", "Panel")

    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256, blank=True)
    abstract = models.TextField(blank=True)
    presentation_type = models.CharField(
        choices=PresentationTypes.choices,
        max_length=18,
    )
    speaker = models.ForeignKey(
        Speaker,
        null=True,
        related_name="presentations",
        on_delete=models.SET_NULL,
    )

    presentation_date = models.DateField(null=True)
    submitted_at = models.DateField(null=True)

    is_accepted = models.BooleanField(null=True)
    accepted_at = models.DateTimeField(null=True)
