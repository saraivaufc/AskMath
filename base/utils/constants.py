from django.utils.translation import ugettext_lazy as _

class Constants():
	#Question
	MESSAGE_SUCCESS_SEND = _("Message send success")
	MESSAGE_ERROR_SEND = _("Error send message")
	#Latex
	HELP_TEXT_LATEX = _("Use <$ and $> to insert latex in text.\
					Example: <$ ax^2 + bx + c = 0 $>")
	#Timezone
	TIMEZONE_SUCCESS_CONFIG = _("Timezone configured success")