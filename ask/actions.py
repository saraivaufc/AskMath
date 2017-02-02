from django.utils.translation import ugettext as _

class StatusAction(object):
	actions = ['make_published', 'make_draft', 'make_withdrawn']

	def make_published(self, request, queryset):
		rows_updated = queryset.update(status='p')
		if rows_updated == 1:
			message_bit = "1 story was"
		else:
			message_bit = "%s stories were" % rows_updated
		self.message_user(request, "%s successfully marked as published." % message_bit)

	def make_draft(self, request, queryset):
		rows_updated = queryset.update(status='d')
		if rows_updated == 1:
			message_bit = "1 story was"
		else:
			message_bit = "%s stories were" % rows_updated
		self.message_user(request, "%s successfully marked as draft." % message_bit)

	def make_withdrawn(self, request, queryset):
		rows_updated = queryset.update(status='w')
		if rows_updated == 1:
			message_bit = "1 story was"
		else:
			message_bit = "%s stories were" % rows_updated
		self.message_user(request, "%s successfully marked as withdrawn." % message_bit)

	make_published.short_description = _("Mark selected stories as published")
	make_draft.short_description = _("Mark selected stories as draft")
	make_withdrawn.short_description = _("Mark selected stories as withdrawn")
