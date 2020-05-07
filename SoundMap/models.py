from django.db import models


# 声音地图主表
class SoundMap(models.Model):
    name = models.CharField(max_length=200, verbose_name='项目名称')
    background_image = models.ImageField(verbose_name='背景图片')
    bak_1 = models.CharField(max_length=200, verbose_name='备注1')
    bak_2 = models.CharField(max_length=200, verbose_name='备注2')
    bak_3 = models.CharField(max_length=200, verbose_name='备注3')


# 声音地图图片明细表
class SoundMapImageItem(models.Model):
    map = models.ForeignKey(SoundMap, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name='素材名称')
    is_show_name = models.CharField(max_length=200, verbose_name='是否显示名称')
    name_size = models.CharField(max_length=200, verbose_name='名称字体大小')
    name_color = models.CharField(max_length=200, verbose_name='名称字体颜色')
    name_loc = models.IntegerField(verbose_name='名称位置')
    loc_left = models.CharField(max_length=200, verbose_name='位置-左')
    loc_top = models.CharField(max_length=200, verbose_name='位置-上')
    size_width = models.CharField(max_length=200, verbose_name='图标宽度')
    size_height = models.CharField(max_length=200, verbose_name='图标高度')
    icon_image = models.ImageField(verbose_name='图标图片')
    content_image = models.URLField(verbose_name='点击后显示内容URL')
    is_show = models.BooleanField(verbose_name='是否显示')


# 声音地图声音明细表
class SoundMapSoundItem(models.Model):
    map = models.ForeignKey(SoundMap, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name='素材名称')
    is_show_name = models.CharField(max_length=200, verbose_name='是否显示名称')
    name_size = models.CharField(max_length=200, verbose_name='名称字体大小')
    name_color = models.CharField(max_length=200, verbose_name='名称字体颜色')
    name_loc = models.IntegerField(verbose_name='名称位置')
    loc_left = models.CharField(max_length=200, verbose_name='位置-左')
    loc_top = models.CharField(max_length=200, verbose_name='位置-上')
    size_width = models.CharField(max_length=200, verbose_name='图标宽度')
    size_height = models.CharField(max_length=200, verbose_name='图标高度')
    pause_image = models.ImageField(verbose_name='静止时显示图片')
    play_image = models.ImageField(verbose_name='播放时显示图片')
    font_size = models.CharField(max_length=200, verbose_name='字体大小')
    font_color = models.CharField(max_length=200, verbose_name='字体颜色')
    sound_file = models.FileField(verbose_name='声音文件')
    sound_length = models.IntegerField(verbose_name='播放时长')
    is_show = models.BooleanField(verbose_name='是否显示')
