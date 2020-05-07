from django.contrib import admin

from .models import SoundMap, SoundMapSoundItem, SoundMapImageItem

# Register your models here.


admin.site.register(SoundMap)
admin.site.register(SoundMapSoundItem)
admin.site.register(SoundMapImageItem)
