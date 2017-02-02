# -*- coding: UTF-8 -*-

from django.utils.translation import ugettext_lazy as _

import random

COLORS = (
	("bg-lime", _(u"Lime")),
	("bg-green", _(u"Green")),
	("bg-emerald", _(u"Emerald")),
	("bg-teal", _(u"Teal")),
	("bg-blue", _(u"Blue")),
	("bg-cyan", _(u"Cyan")),
	("bg-cobalt", _(u"Cobalt")),
	("bg-indigo", _(u"Indigo")),
	("bg-violet", _(u"Violet")),
	("bg-magenta", _(u"Magenta")),
	("bg-orange", _(u"Orange")),
	("bg-amber", _(u"Amber")),
	("bg-yellow", _(u"Yellow")),
	("bg-brown", _(u"Brown")),
	("bg-olive", _(u"Emerald")),
	("bg-steel", _(u"Steel")),
	("bg-mauve", _(u"Mauve")),
	("bg-taupe", _(u"Taupe")),
	("bg-gray", _(u"Gray")),
)

COLORS_DARK = (
	("bg-darkBrown", _(u"Dark Brown")),
	("bg-darkIndigo", _(u"Dark Indigo")),
	("bg-darkCyan", _(u"Dark Cyan")),
	("bg-darkCobalt", _(u"Dark Cobalt")),
	("bg-darkTeal", _(u"Dark Teal")),
	("bg-darkEmerald", _(u"Dark Emerald")),
	("bg-darkGreen", _(u"Dark Green")),
	("bg-darkOrange", _(u"Dark Orange")),
	("bg-darkViolet", _(u"Dark Violet")),
	("bg-darkBlue", _(u"Dark Blue")),
)

COLORS_LIGHT = (
	("bg-lightBlue", _(u"Light Blue")),
	("bg-lightRed", _(u"Light Red")),
	("bg-lightGreen", _(u"Light Green")),
	("bg-lighterBlue", _(u"Lighter Blue")),
	("bg-lightOlive", _(u"Light Olive")),
	("bg-lightOrange", _(u"Light Orange")),
)

COLORS_ALL = COLORS + COLORS_LIGHT + COLORS_DARK


def get_color():
	choose = random.choice(COLORS_ALL)
	return choose[0]