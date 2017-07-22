from blog import settings as local_settings

def load(request):
	context = {}
	context['blog_name'] = local_settings.BLOG_NAME
	return context