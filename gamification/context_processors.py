from .models import LevelManager, ScoreManager

def load(request):
	context = {}
	if request.user.is_authenticated():
		level_manager = LevelManager.objects.get_or_create(user=request.user)[0]
		score_manager = ScoreManager.objects.get_or_create(user=request.user)[0]
		context['level_manager'] = level_manager
		context['score_manager'] = score_manager
	return context