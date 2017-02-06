from django.db import models
from django.utils.translation import ugettext as _
from django.template.defaultfilters import slugify
from django.conf import settings

from base.utils.models import AutoSlugField

from .comment import Comment

STATUS_CHOICES = (
	('d', _('Draft')),
	('p', _('Published')),
	('w', _('Withdrawn')),
)

class Topic(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("user"))
	category = models.ForeignKey('forum.Category', verbose_name=_("Category"))

	title = models.CharField(verbose_name=_("Title"), max_length=75)
	slug = AutoSlugField(populate_from="title", db_index=False, blank=True, unique=True)
	date = models.DateTimeField(verbose_name=_("Date"), auto_now_add=True)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES)
	
	is_closed = models.BooleanField(verbose_name=_("Closed"), default=False)
	is_removed = models.BooleanField(default=False)
	
	view_count = models.PositiveIntegerField(verbose_name=_("Views count"), default=0)
	comment_count = models.PositiveIntegerField(verbose_name=_("Comment count"), default=0)

	def get_comments(self):
		return Comment.objects.filter(topic=self, status='p')

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-date', ]
		verbose_name = _("Topic")
		verbose_name_plural = _("Topics")