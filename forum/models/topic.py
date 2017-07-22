from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse_lazy
from django.conf import settings

from base.utils.models import AutoSlugField

from .comment import Comment

class Topic(models.Model):
	DRAFT = 'd'
	PUBLISHED = 'p'
	REMOVED = 'r'
	STATUS_CHOICES = (
		(DRAFT, _('Draft')),
		(PUBLISHED, _('Published')),
		(REMOVED, _('Removed')),
	)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("user"))
	category = models.ForeignKey('forum.Category', verbose_name=_("Category"))

	slug = AutoSlugField(populate_from="title", db_index=False, blank=True, unique=True)
	title = models.CharField(verbose_name=_("Title"), max_length=75)
	description = models.TextField(verbose_name=_("Description"))
	status = models.CharField(max_length=1, choices=STATUS_CHOICES)
	
	creation = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)
	ip_address = models.GenericIPAddressField(blank=True, null=True)
	
	def get_comments(self):
		return Comment.objects.filter(topic=self, status='p')

	def get_absolute_url(self):
		return reverse_lazy('forum:topic_detail', kwargs={'slug': self.slug})

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-last_modified',]
		verbose_name = _("Topic")
		verbose_name_plural = _("Topics")