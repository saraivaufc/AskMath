from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models import Issue, Lesson
from .serializers import IssueSerializer, LessonSerializer

class IssueList(APIView):
	"""
	List all Issues
	"""
	def get(self, request, format=None):
		disciplines = Issue.objects.filter(status='p')
		serializer = IssueSerializer(disciplines, context={'request': request}, many=True)
		return Response(serializer.data)

class LessonList(APIView):
	"""
	List all lessons
	"""
	def get(self, request, format=None):
		lessons = Lesson.objects.filter(status='p')
		serializer = LessonSerializer(lessons, context={'request': request}, many=True)
		return Response(serializer.data)