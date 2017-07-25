from django.http import Http404

from rest_framework import generics

from rest_framework.response import Response

from ..models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer

class CourseListCreateAPIView(generics.ListCreateAPIView):
	serializer_class = CourseSerializer
	queryset = Course.objects.filter(status=Course.PUBLISHED)

class LessonListCreateAPIView(generics.ListCreateAPIView):
	serializer_class = LessonSerializer
	queryset = Lesson.objects.filter(status=Lesson.PUBLISHED)