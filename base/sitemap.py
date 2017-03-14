
from ask.models import Course, Lesson, Question

courses = {
	'queryset': Course.objects.filter(status='p'),
	'date_field': 'last_modified',
}

lessons = {
	'queryset': Lesson.objects.filter(status='p'),
	'date_field': 'last_modified',
}

from forum.models import Topic


topics = {
	'queryset': Topic.objects.filter(status='p'),
	'date_field': 'last_modified',
}