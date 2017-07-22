from django.contrib import admin

from .models import (Challenge, Solution,)
from .forms import (ChallengeForm, SolutionForm,)

class SolutionInline(admin.TabularInline):
	model = Solution
	fields = ['text','is_correct',]
	extra = 0

class ChallengeAdmin(admin.ModelAdmin):
	form = ChallengeForm
	list_display = ('title', 'level', 'status', 'last_modified')
	list_filter = ['status', 'creation', 'last_modified']
	search_fields = ['title']

	inlines = [
		SolutionInline,
	]

	def save_model(self, request, obj, form, change):
		form.instance.created_by = request.user
		form.save()

admin.site.register(Challenge, ChallengeAdmin)