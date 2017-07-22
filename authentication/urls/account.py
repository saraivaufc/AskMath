from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required

from authentication.views import AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView, AccountActivateView

urlpatterns = [
	url(_(r'^login$'), auth_views.login, {'template_name': 'authentication/account/login.html',}, name="account_login"),
	url(_(r'^logout$'), login_required(auth_views.logout), {'next_page': reverse_lazy("authentication:account_login")}, name="account_logout"),
	url(_(r'^register$'), AccountCreateView.as_view(), name="account_register"),
	url(_(r'^(?P<pk>[0-9]+)/detail$'), AccountDetailView.as_view(), name="account_detail"),
	url(_(r'^(?P<pk>[0-9]+)/edit$'), AccountUpdateView.as_view(), name="account_update"),
	url(_(r'^(?P<pk>[0-9]+)/delete$'), AccountDeleteView.as_view(), name="account_delete"),

	url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/activate/$', 
		AccountActivateView.as_view(), name='account_activate'),

	url(_(r'^password/change$'), auth_views.password_change, 
	 	{'template_name': 'authentication/account/password_change_form.html',
	 	'post_change_redirect': reverse_lazy("authentication:account_password_change_done"),
	 	},
	 	name='account_password_change', 
	 ),

	 url(_(r'^password_change/done$'), auth_views.password_change_done, 
	 	{'template_name': 'authentication/account/password_change_done.html',},
	 	name='account_password_change_done'
	 ),

	url(_(r'^password/reset$'), auth_views.password_reset, 
	 	{'template_name': 'authentication/account/password_reset_form.html',
	 	'post_reset_redirect': reverse_lazy("authentication:account_password_reset_done"),
	 	'email_template_name': 'authentication/account/password_reset_email.html',},
	 	name='account_password_reset', 
	 ),

	 url(_(r'^password_reset/done$'), auth_views.password_reset_done, 
	 	{'template_name': 'authentication/account/password_reset_done.html',},
	 	name='account_password_reset_done'),

	 url(_(r'^password_reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)$'), auth_views.password_reset_confirm,
	 	{'template_name': 'authentication/account/password_reset_confirm.html',
	 	'post_reset_redirect': reverse_lazy("authentication:account_password_reset_complete"),}, 
	 	name='account_password_reset_confirm'),
	 
	url(_(r'^password_reset/complete$'), auth_views.password_reset_complete,
	 	{'template_name': 'authentication/account/password_reset_complete.html',},  
	 	name='account_password_reset_complete'),
]
