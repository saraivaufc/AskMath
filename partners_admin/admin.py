from django.utils.encoding import force_text, python_2_unicode_compatible
from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.conf.urls import url
from django.template.response import TemplateResponse

from .actions import SortableAction

#Base
from base.models import SocialNetwork
from base.admin import SocialNetworkAdmin

#Ask
from ask.models import Issue, Lesson, Question, Video, Answer
from ask.admin import IssueAdmin, LessonAdmin, QuestionAdmin, VideoAdmin, AnswerAdmin

#Forum
from forum.models import Category, Topic, Comment
from forum.admin import CategoryAdmin, TopicAdmin, CommentAdmin

#Authentication
from authentication.models import User
from django.contrib.auth.models import Group, Permission
from authentication.admin import UserAdmin, GroupAdmin, PermissionAdmin

#FlatPage
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin

#LogEntry
from django.contrib.admin.models import LogEntry

#LogEntry
from django.contrib.sessions.models import Session

#Sites
from django.contrib.sites.models import Site
from django.contrib.sites.admin import SiteAdmin

class PartnersAdminSite(AdminSite):
	site_header = _(u"AskMath - Administration")
	site_title = _(u"AskMath - Site Administration")
	index_title = _(u"Applications")

class LogEntryPartnerAdmin(admin.ModelAdmin):
	list_display = [ '__str__', 'content_type', 'user', 'action_time']
	list_filter = ['user', 'action_time', 'content_type', ]

class SessionPartnerAdmin(admin.ModelAdmin):
	list_display = [ 'session_key', 'expire_date']
	#list_filter = ['user', 'action_time', 'content_type', ]
	
class LessonPartnerAdmin(LessonAdmin, SortableAction):
	list_display = ('name', 'status', 'sort_questions', 'sort_videos',)
	model = Lesson

	def get_urls(self):
		info = self.model._meta.app_label, self.model._meta.model_name
		urls = super(LessonPartnerAdmin, self).get_urls()
		my_urls = [
			url(r'^(?P<pk>[0-9]+)/sort_questions/$', self.admin_site.admin_view(self.sort_questions_view, cacheable=True) , name='%s_%s_sort_questions' % info),
			url(r'^(?P<pk>[0-9]+)/sort_videos/$', self.admin_site.admin_view(self.sort_videos_view, cacheable=True) , name='%s_%s_sort_videos' % info),
		]
		return my_urls + urls

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

	def sort_questions_view(self, request, pk):
		context = super(LessonPartnerAdmin, self).get_context(request)
		
		object = Lesson.objects.get(pk=pk)
		results = object.questions.all()
		context.update({'object':object, 'results':results,})

		if request.method == 'POST':
			self.sort_fields(request, Question,  len(results))
			return HttpResponseRedirect(request.path)
		return TemplateResponse(request, "partners_admin/question/sort.html", context)

	def sort_videos_view(self, request, pk):
		context = super(LessonPartnerAdmin, self).get_context(request)
		
		object = Lesson.objects.get(pk=pk)
		results = object.videos.all()
		context.update({'object':object,'results':results})
		
		if request.method == 'POST':
			self.sort_fields(request, Video, len(results))
			return HttpResponseRedirect(request.path)
		return TemplateResponse(request, "partners_admin/video/sort.html", context)
	
partners_admin = PartnersAdminSite(name='partners_admin')

#Base
partners_admin.register(SocialNetwork, SocialNetworkAdmin)

#Ask
partners_admin.register(Issue, IssueAdmin)
partners_admin.register(Lesson, LessonPartnerAdmin)
partners_admin.register(Question, QuestionAdmin)
partners_admin.register(Video, VideoAdmin)
partners_admin.register(Answer, AnswerAdmin)

#Forum
partners_admin.register(Category, CategoryAdmin)
partners_admin.register(Topic, TopicAdmin)
partners_admin.register(Comment, CommentAdmin)

#Authentication
partners_admin.register(User, UserAdmin)
partners_admin.register(Group, GroupAdmin)
partners_admin.register(Permission, PermissionAdmin)

#Flatpage
partners_admin.register(FlatPage, FlatPageAdmin)

#LogEntry
partners_admin.register(LogEntry, LogEntryPartnerAdmin)

#Session
partners_admin.register(Session, SessionPartnerAdmin)

#Site
partners_admin.register(Site, SiteAdmin)