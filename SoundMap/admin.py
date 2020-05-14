from django.contrib import admin

from .models import SoundMap, Audio, Image, Video


class AudioInline(admin.TabularInline):
    model = Audio
    fieldsets = [
        (
            '名称信息', {'fields': ['name', 'is_show_name', 'name_size', 'name_color', 'name_loc']}
        ),
        (
            '位置信息', {'fields': ['loc_left', 'loc_top', 'size_width', 'size_height', 'is_show']}
        ),
        (
            '内容信息', {'fields': ['pause_image', 'play_image', 'sound_file', 'sound_length']}
        ),

    ]
    extra = 0


class VideoInline(admin.TabularInline):
    model = Video
    fieldsets = [
        (
            '名称信息', {'fields': ['name', 'is_show_name', 'name_size', 'name_color', 'name_loc']}
        ),
        (
            '位置信息', {'fields': ['loc_left', 'loc_top', 'size_width', 'size_height', 'is_show']}
        ),
        (
            '内容信息', {'fields': ['pause_image', 'play_image', 'video_file', 'video_length']}
        ),

    ]
    extra = 0


class ImageInline(admin.TabularInline):
    model = Image
    fieldsets = [
        (
            '名称信息', {'fields': ['name', 'is_show_name', 'name_size', 'name_color', 'name_loc']}
        ),
        (
            '位置信息', {'fields': ['loc_left', 'loc_top', 'size_width', 'size_height', 'is_show']}
        ),
        (
            '内容信息', {'fields': ['icon_image', 'content_image']}
        ),

    ]
    extra = 0


class SoundMapAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'background_image']})
    ]
    inlines = [AudioInline, VideoInline, ImageInline]
    list_display = ('name', 'background_image', 'bak_1', 'bak_2', 'bak_3')
    search_fields = ['name']


admin.site.register(SoundMap, SoundMapAdmin)
