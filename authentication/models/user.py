from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy
from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
	Group,
	BaseUserManager, 
	AbstractBaseUser, 
	PermissionsMixin, 
)
from django.utils import timezone
from django.template.defaultfilters import slugify

from authentication import settings as local_settings

class UserManager(BaseUserManager):
	def create_user(self, email, first_name, last_name, password, group='default'):
		if not email:
			raise ValueError('Users must have an email address')
		user = self.model(
			first_name=first_name,
			last_name=last_name,
			email=self.normalize_email(email),
		)
		user.set_password(password)
		user.save(group=group)
		return user
	def create_superuser(self, email, first_name, last_name,  password, group='administrator'):
		user = self.create_user(email,
			first_name=first_name,
			last_name=last_name,
			password=password,
		)
		user.is_superuser = True
		user.is_moderator = True
		user.is_staff = True
		user.save(group=group)
		return user


class User(AbstractBaseUser, PermissionsMixin):
	first_name = models.CharField(verbose_name=_("First Name"), max_length=100, blank=False, null=False, help_text=_(u'Please enter you first name.'), )
	last_name = models.CharField(verbose_name=_("Last Name"), max_length=100, blank=False, null=False, help_text=_(u'Please enter you last name.'), )
	email = models.EmailField(verbose_name=_("Email"), max_length=254, unique=True,  null=False, blank=False, help_text=_(u'Please enter you email.'), )
	profile_image = models.ImageField(verbose_name=_("Profile Image"), upload_to=local_settings.PROFILE_IMAGE_DIR, null=True, blank=True)
	is_active = models.BooleanField(verbose_name=_('Active'), default=True, help_text=_(u'Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))
	date_joined = models.DateTimeField(verbose_name=_(u'Date joined'), default=timezone.now)
	is_moderator = models.BooleanField(_('Moderator Status'), default=False, blank=True)
	is_staff = models.BooleanField(_(u'Staff Status'), default=False,)
	
	REQUIRED_FIELDS =['first_name', 'last_name', ]
	USERNAME_FIELD = 'email'

	objects = UserManager()

	def get_full_name(self):
		if self.first_name and self.last_name:
			return self.first_name + ' ' + self.last_name
		elif self.first_name:
			return first_name
		elif self.last_name:
			return self.last_name
		else:
			return self.id

	def get_short_name(self):
		return self.last_name

	def save(self, group=None, *args, **kwargs):
		user = super(User, self).save()
		if group:
			group = Group.objects.get(name=group)
			self.groups.add(group)

	def __unicode__(self):
		return "{0} - {1}".format(self.get_full_name(), self.email)

	def natural_key(self):
		return self.email

	def verbose_name(self):
		return self._meta.verbose_name

	def get_absolute_url(self):
		return reverse_lazy('authentication:account_detail', kwargs={'pk': self.pk})

	class Meta:
		verbose_name = _(u'User')
		verbose_name_plural = _(u'Users')