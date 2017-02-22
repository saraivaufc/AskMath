from django.utils.translation import ugettext_lazy as _

class StatusAction(object):
	actions = ['make_published', 'make_draft', 'make_removed']

	def make_published(self, request, queryset):
		rows_updated = queryset.update(status='p')
		if rows_updated == 1:
			message_bit = _(u"1 story was")
		else:
			message_bit = _(u"%s stories were" % rows_updated)
		self.message_user(request,_(u"%s successfully marked as published." % message_bit))

	def make_draft(self, request, queryset):
		rows_updated = queryset.update(status='d')
		if rows_updated == 1:
			message_bit = _(u"1 story was")
		else:
			message_bit = _(u"%s stories were" % rows_updated)
		self.message_user(request,_(u"%s successfully marked as draft." % message_bit))

	def make_removed(self, request, queryset):
		rows_updated = queryset.update(status='r')
		if rows_updated == 1:
			message_bit = _(u"1 story was")
		else:
			message_bit = _(u"%s stories were" % rows_updated)
		self.message_user(request,_(u"%s successfully marked as removed." % message_bit))

	make_published.short_description = _("Mark selected stories as published")
	make_draft.short_description = _("Mark selected stories as draft")
	make_removed.short_description = _("Mark selected stories as removed")
