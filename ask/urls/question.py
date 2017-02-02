from django.conf.urls import include, url
from django.utils.translation import ugettext_lazy as _

from ask.views import QuestionDetailView

urlpatterns = [
	url(_(r'^answer_question/$'), QuestionDetailView.as_view(), name="answer_question"),
]