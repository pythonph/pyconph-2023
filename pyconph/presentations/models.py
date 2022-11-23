from django.db import models


class Speaker(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64, blank=True)
    title = models.CharField(
        max_length=128,
        blank=True,
        help_text="Short title to call the speaker, eg: CEO of X company",
    )
    display_photo = models.ImageField()


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
