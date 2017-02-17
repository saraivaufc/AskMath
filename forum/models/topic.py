from django.db import models
from django.utils.translation import ugettext as _
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse_lazy
from django.conf import settings

from base.utils.models import AutoSlugField

from .comment import Comment

STATUS_CHOICES = (
	('d', _('Draft')),
	('p', _('Published')),
	('r', _('Removed')),
)

class Topic(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("user"))
	category = models.ForeignKey('forum.Category', verbose_name=_("Category"))

	title = models.CharField(verbose_name=_("Title"), max_length=75)
	slug = AutoSlugField(populate_from="title", db_index=False, blank=True, unique=True)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES)
	
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u"Created by"), related_name="topic_created_by", blank=True)
	creation = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)
	
	def get_comments(self):
		return Comment.objects.filter(topic=self, status='p')

	def get_absolute_url(self):
		return reverse_lazy('forum:topic_detail', kwargs={'category_slug': self.category.slug, 'slug': self.slug})

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-last_modified',]
		verbose_name = _("Topic")
		verbose_name_plural = _("Topics")