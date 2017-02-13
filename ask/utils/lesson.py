# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ask.utils.functions import lists_to_list
from ask.models import Answer

class LessonSorting():
	def __init__(self, lessons):
		self.__lessons = lessons
		self.__level_lesson = {}
		self.__index_level = 1

	def visit(self, lesson):
		#verifico se a lição que estou visitando já foi visitada antes
		if lesson in lists_to_list(self.__level_lesson.values()):
			return
		#agora pego todos os pré-requisitos que ela possue
		requirements = lesson.requirements.filter(status='p')
		#verifico se todos os pré-requisitos já foram atendidos 
		if (set( lists_to_list(self.__level_lesson.values()) )).issuperset(set(requirements)):	
			#se todos os pré-requisitos já foram atendidos, então eu pego o nivel mais alto que estão seus pré-requisitos
			try:
				max_level = max(map(lambda x: self.get_level_lesson(x) , requirements)) 
			except Exception, e:
				print e
				return
			#o nível que essa lição irá ficar é um nível acima ao mais alto nível dos seus pré-requisitos
			self.__index_level = max_level + 1
			if not self.__level_lesson.has_key(self.__index_level):
				self.__level_lesson[self.__index_level] = []
			#termino de visitar a lição
			self.__level_lesson[self.__index_level].append(lesson)
		else:
			#se ainda existir pré-requisitos que ainda não foram atendidos, eu visito(atendo) eles
			for requirement in requirements:
				self.visit(requirement)

	def get_level_lesson(self, lesson):
		for level, lessons in self.__level_lesson.items():
			if lesson in lessons:
				return level
		return 0

	def get_lessons(self):
		#primeiramente, insiro todas as licoes que nao possuem requisitos publicados
		self.__level_lesson[self.__index_level] = self.__lessons.filter(status='p').exclude(requirements__status__contains='p')
		#agora visito apenas as licoes que possuem requisitos
		map(lambda x: self.visit(x), self.__lessons.filter(status='p', requirements__status__contains='p'))
		return self.__level_lesson

def get_question_of_lesson(user, lesson):
	questions = list(lesson.questions.all().order_by('position'))
	questions_ = []
	#primeiramente, pego todas as questoes que ainda nao foram respondidas
	for index, question in enumerate(questions):
		if not Answer.objects.filter(user=user, question=question, exists=True).exists():
			questions_.append(question)
	#se nao existir mais questoes para serem respondidas, entao eu pego a resposta incorreta mais antiga
	if not questions_:
		answer = Answer.objects.filter(user=user, lesson=lesson, correct=False, exists=True).last()
		if answer:
			return answer.question

	if len(questions_) >= 1:
		return questions_[0]
	else:
		return None