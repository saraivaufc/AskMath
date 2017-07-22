from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from base.utils.models import AutoSlugField

from .post import Post

class Category(models.Model):
	slug = AutoSlugField(populate_from="name", db_index=False, blank=True, unique=True)
	name = models.CharField(verbose_name=_("Name"), max_length=100)
	creation = models.DateTimeField(verbose_name=(_("Creation")), auto_now_add=True)

	def get_posts(self):
		return Post.objects.filter(categories=self)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['name']
		verbose_name = _("Category")
		verbose_name_plural = _("Categories")