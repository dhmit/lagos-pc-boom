from django.db import models

from wagtail.images.models import Image, AbstractImage, AbstractRendition

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

# @register_snippet
# class NavBar(models.Model):
#     """
#     This is the navigation bar model
#     """
#     name = models.CharField(max_length=255)
#     # menu_items =

class FrontMatter(Page):
    header = models.CharField(max_length=30, null=True)
    info = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('header'),
        FieldPanel('info', classname="full"),
    ]

class LagosImage(AbstractImage):

    obj_num = models.CharField("Object Number", max_length=20, null=True)
    title = models.CharField(max_length=75, null=True)
    publisher = models.CharField(max_length=50, null=True)
    creator = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=100, null=True)
    date = models.DateField("Date", null=True)
    num_of_pages = models.CharField("Page Number(s)", max_length=10, null=True)
    subject = models.CharField(max_length=100, null=True)
    language = models.CharField(max_length=30, null=True)
    genre = models.CharField(max_length=50, null=True)
    notes = models.CharField(max_length=100, null=True)
    specific_notes = models.CharField("Specific Notes", max_length=200, null=True)

    admin_form_fields = Image.admin_form_fields + (
        'obj_num',
        'title',
        'publisher',
        'creator',
        'location',
        'date',
        'num_of_pages',
        'subject',
        'language',
        'genre',
        'notes',
        'specific_notes',
    )

class LagosImageRendition(AbstractRendition):
    image = models.ForeignKey(LagosImage, on_delete=models.CASCADE, related_name='renditions')

    class Meta:
        unique_together = (
            ('image', 'filter_spec', 'focal_point_key'),
        )