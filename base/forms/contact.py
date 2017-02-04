from django.utils.translation import ugettext_lazy as _
from django import forms

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100, label=_(u"Subject"))
	message = forms.CharField(max_length=300, label=_(u"Message"), widget=forms.Textarea(attrs={'rows': 2}))
	email = forms.EmailField(label=_(u"Email"))
