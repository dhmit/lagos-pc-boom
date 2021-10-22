from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page

from wagtail.images.models import Image
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index


# Create your models here.
class BlogIndexPage(Page):
    intro = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

class BlogPage(Page):
    date = models.DateField("Post date")
    author = models.CharField(max_length=30, null=True)
    intro = models.CharField(max_length=250, null=True)
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('author'),
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('author'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
    ]
