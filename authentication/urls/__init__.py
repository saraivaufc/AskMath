from django.conf.urls import include, url
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
	url(_(r'^account/'), include('authentication.urls.account')),
]
