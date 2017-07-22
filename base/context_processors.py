from base import settings as local_settings

def load(request):
	context = {}
	context['site_name'] = local_settings.SITE_NAME
	context['site_description'] = local_settings.SITE_DESCRIPTION
	context['site_author'] = local_settings.SITE_AUTHOR
	context['site_url'] = local_settings.SITE_URL
	return context