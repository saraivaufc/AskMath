from django.utils.translation import ugettext_lazy as _
from django.conf.urls import url
from .views import CourseListCreateAPIView, LessonListCreateAPIView

urlpatterns = (
    url(_(r'^course/$'), CourseListCreateAPIView.as_view(), name='api_course'),
    url(_(r'^lesson/$'), LessonListCreateAPIView.as_view(), name='api_lesson'),
)