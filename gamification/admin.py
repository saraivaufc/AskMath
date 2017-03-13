from django.contrib import admin

from .models import (Level, LevelManager, RankingManager, ScoreManager)

class LevelAdmin(admin.ModelAdmin):
	model = Level
	list_display = ('name', 'number')

class LevelManagerAdmin(admin.ModelAdmin):
	model = LevelManager
	list_display = ('user', 'level')

class RankingManagerAdmin(admin.ModelAdmin):
	model = RankingManager
	list_display = ()

class ScoreManagerAdmin(admin.ModelAdmin):
	model = ScoreManager
	list_display = ('user', 'xp', 'rp', 'skill', 'reputation')

admin.site.register(Level, LevelAdmin)
admin.site.register(LevelManager, LevelManagerAdmin)
admin.site.register(RankingManager, RankingManagerAdmin)
admin.site.register(ScoreManager, ScoreManagerAdmin)