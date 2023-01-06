from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class ContentPage(Page):
    content_title = models.CharField(max_length=255)
    content_subtitle = models.CharField(max_length=255, blank=True)
    content_body = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('content_title'),
        FieldPanel('content_subtitle'),
        FieldPanel('content_body'),
    ]
