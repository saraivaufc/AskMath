from rest_framework import serializers

from ..models import Issue, Lesson


class IssueSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Issue
		fields = ('name', 'slug')

class LessonSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Lesson
		fields = ('name', 'slug')
