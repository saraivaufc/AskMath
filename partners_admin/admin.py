from django.utils.encoding import force_text, python_2_unicode_compatible
from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy
from django.conf.urls import url
from django.template.response import TemplateResponse

from partners_admin.urls import partners_admin_urls

from ask.models import Issue, Lesson, Question, Video
from ask.admin import IssueAdmin, LessonAdmin, QuestionAdmin, VideoAdmin

class PartnersAdminSite(AdminSite):
	site_header = _(u"AskMath Administration")

	def get_urls(self):
		new_registry = {}
		allowed_models = [Issue, Lesson, Question, Video]
		for model, admin_model in self._registry.items():
			if model in allowed_models:
				new_registry[model] = admin_model
		self._registry = new_registry
		
		urlpatterns = super(PartnersAdminSite, self).get_urls()
		urlpatterns += partners_admin_urls()
		return urlpatterns
		
class LessonPartnerAdmin(LessonAdmin):
	list_display = ('name', 'status', 'sort_questions', 'sort_videos',)
	model = Lesson

	def sort_questions(self, obj):
		return format_html("<a href='{}'>{}</a>",
			reverse_lazy("admin:{}_{}_sort_questions".format(self.model._meta.app_label, self.model._meta.model_name), kwargs={'pk':obj.pk}),
			_(u"Sort {count} Questions".format(count=len(obj.questions.all()) ) ),
		)

	def sort_videos(self, obj):
		return format_html("<a href='{}'>{}</a>",
			reverse_lazy("admin:{}_{}_sort_videos".format(self.model._meta.app_label, self.model._meta.model_name), kwargs={'pk':obj.pk}),
			_(u"Sort {count} Videos".format(count=len(obj.videos.all()) ) ),
		)

	def get_urls(self):
		#reference in 709
		info = self.model._meta.app_label, self.model._meta.model_name
		urls = super(LessonPartnerAdmin, self).get_urls()
		my_urls = [
			url(r'^(?P<pk>[0-9]+)/sort_questions/$', self.admin_site.admin_view(self.sort_questions_view, cacheable=True) , name='%s_%s_sort_questions' % info),
			url(r'^(?P<pk>[0-9]+)/sort_videos/$', self.admin_site.admin_view(self.sort_videos_view, cacheable=True) , name='%s_%s_sort_videos' % info),
		]
		return my_urls + urls

	def sort_fields(self, request, model, count):
		if request.method == 'POST':
			for i in range(1, count+1):
				if request.POST.has_key('result_{}'.format(i)):
					result = request.POST['result_{}'.format(i)]
					model.objects.filter(pk=result).update(position=i)
			return True
		else:
			return False


	def sort_questions_view(self, request, pk):
		opts = self.model._meta
		object = Lesson.objects.get(pk=pk)
		results = object.questions.all()
		
		context = dict(
			self.admin_site.each_context(request),
			opts=opts,
			object=object,
			has_change_permission=True,
			results=results,
		)

		if request.method == 'POST':
			self.sort_fields(request, Question,  len(results))
			request.method = "GET"
			return self.sort_questions_view(request, pk)
		
		return TemplateResponse(request, "partners_admin/question/sort.html", context)


	def sort_videos_view(self, request, pk):
		opts = self.model._meta
		object = Lesson.objects.get(pk=pk)
		results = object.videos.filter(status='p')
		
		context = dict(
			self.admin_site.each_context(request),
			opts=opts,
			object=object,
			has_change_permission=True,
			results=results,
		)

		if request.method == 'POST':
			self.sort_fields(request, Video, len(results))
			request.method = "GET"
			return self.sort_videos_view(request, pk)
		
		return TemplateResponse(request, "partners_admin/video/sort.html", context)
	
partners_admin = PartnersAdminSite(name='partners_admin')

partners_admin.register(Issue, IssueAdmin)
partners_admin.register(Lesson, LessonPartnerAdmin)
partners_admin.register(Question, QuestionAdmin)
partners_admin.register(Video, VideoAdmin)

