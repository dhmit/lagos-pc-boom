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
