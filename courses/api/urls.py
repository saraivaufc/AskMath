from django.utils.translation import ugettext_lazy as _
from django.conf.urls import url
from .views import CourseList, LessonList

urlpatterns = (
    url(_(r'^course/$'), CourseList.as_view(), name='api_course'),
    url(_(r'^lesson/$'), LessonList.as_view(), name='api_lesson'),
)