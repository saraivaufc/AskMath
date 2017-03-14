from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer

class CourseList(APIView):
	"""
	List all Courses
	"""
	def get(self, request, format=None):
		disciplines = Course.objects.filter(status='p')
		serializer = CourseSerializer(disciplines, context={'request': request}, many=True)
		return Response(serializer.data)

class LessonList(APIView):
	"""
	List all lessons
	"""
	def get(self, request, format=None):
		lessons = Lesson.objects.filter(status='p')
		serializer = LessonSerializer(lessons, context={'request': request}, many=True)
		return Response(serializer.data)