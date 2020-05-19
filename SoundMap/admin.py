from django.contrib import admin

from .models import SoundMap, Audio, Image, Video


class AudioInline(admin.StackedInline):
    model = Audio
    fieldsets = [
        (
            '名称信息',
            {
                'fields':
                    [
                        ('name', 'is_show_name', 'name_loc'),
                        ('name_size', 'name_color')
                    ]
            }
        ),
        (
            '位置信息',
            {
                'fields':
                    [
                        ('loc_left', 'loc_top', 'is_show')
                    ]
            }
        ),
        (
            '内容信息',
            {
                'fields':
                    [
                        ('play_image', 'pause_image'),
                        ('size_width', 'size_height'),
                        ('sound_file', 'sound_length')
                    ]
            }
        ),
    ]
    extra = 0


class VideoInline(admin.StackedInline):
    model = Video
    fieldsets = [
        (
            '名称信息',
            {
                'fields':
                    [
                        ('name', 'is_show_name', 'name_loc'),
                        ('name_size', 'name_color')
                    ]
            }
        ),
        (
            '位置信息',
            {
                'fields':
                    [
                        ('loc_left', 'loc_top', 'is_show')
                    ]
            }
        ),
        (
            '内容信息',
            {
                'fields':
                    [
                        ('pause_image', 'size_width', 'size_height'),
                        ('video_file', 'video_length')
                    ]
            }
        ),

    ]
    extra = 0


class ImageInline(admin.StackedInline):
    model = Image
    fieldsets = [
        (
            '名称信息',
            {
                'fields':
                    [
                        ('name', 'is_show_name', 'name_loc'),
                        ('name_size', 'name_color')
                    ]
            }
        ),
        (
            '位置信息',
            {
                'fields':
                    [
                        ('loc_left', 'loc_top', 'is_show')
                    ]
            }
        ),
        (
            '内容信息',
            {
                'fields':
                    [
                        ('icon_image', 'size_width', 'size_height'),
                        'content'
                    ]
            }
        ),
    ]
    extra = 0


class SoundMapAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                'fields':
                    [
                        'name',
                        'background_image',
                        ('bak_1', 'bak_2', 'bak_3')
                    ]
            }
        )
    ]
    inlines = [AudioInline, VideoInline, ImageInline]
    list_display = ('name', 'background_image', 'bak_1', 'bak_2', 'bak_3')
    search_fields = ['name']


admin.site.register(SoundMap, SoundMapAdmin)
