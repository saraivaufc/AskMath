from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from base.utils.models import AutoSlugField

from blog import settings as local_settings

class Post(models.Model):
	slug = AutoSlugField(populate_from="title", db_index=False, blank=True, unique=True)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Author"), related_name="post_author", blank=True, limit_choices_to={'is_staff': True})
	title = models.CharField(verbose_name=_("Title"), max_length=100)
	description = models.TextField(verbose_name=_("Description"))
	image = models.ImageField(verbose_name=_("Image"), upload_to=local_settings.POST_IMAGE_DIR, null=True, blank=True)
	categories = models.ManyToManyField('blog.Category', verbose_name=_("Categories"), blank=True)
	creation = models.DateTimeField(verbose_name=(_("Creation")), auto_now_add=True)

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-creation']
		verbose_name = _("Post")
		verbose_name_plural = _("Posts")