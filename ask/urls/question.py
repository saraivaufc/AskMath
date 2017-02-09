from django.conf.urls import include, url
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required

from ask.views import QuestionDetailView

urlpatterns = [
	url(_(r'^answer$'), login_required(QuestionDetailView.as_view()), name="answer_question"),
]