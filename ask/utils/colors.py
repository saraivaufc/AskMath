# -*- coding: UTF-8 -*-

from django.utils.translation import ugettext_lazy as _

import random

COLORS = (
	("bg-lime", "Lime"),
	("bg-green", "Green"),
	("bg-emerald", "Emerald"),
	("bg-teal", "Teal"),
	("bg-blue", "Blue"),
	("bg-cyan", "Cyan"),
	("bg-cobalt", "Cobalt"),
	("bg-indigo", "Indigo"),
	("bg-violet", "Violet"),
	("bg-magenta", "Magenta"),
	("bg-orange", "Orange"),
	("bg-amber", "Amber"),
	("bg-yellow", "Yellow"),
	("bg-brown", "Brown"),
	("bg-olive", "Emerald"),
	("bg-steel", "Steel"),
	("bg-mauve", "Mauve"),
	("bg-taupe", "Taupe"),
	("bg-gray", "Gray"),
)

COLORS_DARK = (
	("bg-darkBrown", "Dark Brown"),
	("bg-darkIndigo", "Dark Indigo"),
	("bg-darkCyan", "Dark Cyan"),
	("bg-darkCobalt", "Dark Cobalt"),
	("bg-darkTeal", "Dark Teal"),
	("bg-darkEmerald", "Dark Emerald"),
	("bg-darkGreen", "Dark Green"),
	("bg-darkOrange", "Dark Orange"),
	("bg-darkViolet", "Dark Violet"),
	("bg-darkBlue", "Dark Blue"),
)

COLORS_LIGHT = (
	("bg-lightBlue", "Light Blue"),
	("bg-lightRed", "Light Red"),
	("bg-lightGreen", "Light Green"),
	("bg-lighterBlue", "Lighter Blue"),
	("bg-lightOlive", "Light Olive"),
	("bg-lightOrange", "Light Orange"),
)

COLORS_ALL = COLORS + COLORS_LIGHT + COLORS_DARK


def get_color():
	choose = random.choice(COLORS_ALL)
	return choose[0]