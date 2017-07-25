from rest_framework import serializers

from ..models import Course, Lesson

class CourseSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Course
		fields = ('pk', 'name', 'description', 'get_absolute_url')

class LessonSerializer(serializers.ModelSerializer):
	class Meta:
		model = Lesson
		fields = ('pk', 'name', 'description', 'courses', 'requirements')