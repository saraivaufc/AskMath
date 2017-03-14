from rest_framework import serializers

from ..models import Course, Lesson


class CourseSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Course
		fields = ('name', 'slug')

class LessonSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Lesson
		fields = ('name', 'slug')
