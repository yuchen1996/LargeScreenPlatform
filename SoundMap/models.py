from django.db import models


LOCATION_CHOICES = (
        (1, '上'),
        (2, '下'),
        (3, '左'),
        (4, '右'),
    )


# 声音地图主表
class SoundMap(models.Model):
    name = models.CharField(max_length=20, verbose_name='项目名称')
    background_image = models.ImageField(verbose_name='背景图片', upload_to='img/%Y/%m/%d', blank=True, null=True)
    bak_1 = models.CharField(max_length=20, verbose_name='备注1', blank=True, null=True)
    bak_2 = models.CharField(max_length=20, verbose_name='备注2', blank=True, null=True)
    bak_3 = models.CharField(max_length=20, verbose_name='备注3', blank=True, null=True)

    class Meta:
        verbose_name = '声音地图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 声音地图声音明细表
class Audio(models.Model):
    map = models.ForeignKey(SoundMap, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, verbose_name='名称')
    is_show_name = models.BooleanField(verbose_name='显示名称', default=True)
    name_size = models.CharField(max_length=20, verbose_name='名称大小', blank=True, null=True)
    name_color = models.CharField(max_length=20, verbose_name='名称颜色', blank=True, null=True, default='#000')
    name_loc = models.IntegerField(verbose_name='名称位置', choices=LOCATION_CHOICES)
    loc_left = models.CharField(max_length=20, verbose_name='位置-左')
    loc_top = models.CharField(max_length=20, verbose_name='位置-上')
    size_width = models.CharField(max_length=20, verbose_name='图标宽度', blank=True, null=True)
    size_height = models.CharField(max_length=20, verbose_name='图标高度', blank=True, null=True)
    play_image = models.ImageField(verbose_name='播放显示图片')
    pause_image = models.ImageField(verbose_name='静止显示图片')
    sound_file = models.FileField(verbose_name='声音文件')
    sound_length = models.IntegerField(verbose_name='播放时长', blank=True, null=True)
    is_show = models.BooleanField(verbose_name='显示', default=True)

    class Meta:
        verbose_name = '声音元素'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 声音地图图片明细表
class Image(models.Model):
    map = models.ForeignKey(SoundMap, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, verbose_name='名称')
    is_show_name = models.BooleanField(verbose_name='显示名称', default=False)
    name_size = models.CharField(max_length=20, verbose_name='名称大小', blank=True, null=True)
    name_color = models.CharField(max_length=20, verbose_name='名称颜色', blank=True, null=True)
    name_loc = models.IntegerField(verbose_name='名称位置', choices=LOCATION_CHOICES)
    loc_left = models.CharField(max_length=20, verbose_name='位置-左')
    loc_top = models.CharField(max_length=20, verbose_name='位置-上')
    size_width = models.CharField(max_length=20, verbose_name='图标宽', blank=True, null=True)
    size_height = models.CharField(max_length=20, verbose_name='图标高', blank=True, null=True)
    icon_image = models.ImageField(verbose_name='图片')
    content = models.URLField(verbose_name='内容URL', blank=True, null=True)
    is_show = models.BooleanField(verbose_name='显示', default=True)

    class Meta:
        verbose_name = '图片元素'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 声音地图视频明细表
class Video(models.Model):
    map = models.ForeignKey(SoundMap, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, verbose_name='名称')
    is_show_name = models.BooleanField(verbose_name='显示名称', default=True)
    name_size = models.CharField(max_length=20, verbose_name='名称大小', blank=True, null=True)
    name_color = models.CharField(max_length=20, verbose_name='名称颜色', blank=True, null=True, default='#000')
    name_loc = models.IntegerField(verbose_name='名称位置', choices=LOCATION_CHOICES)
    loc_left = models.CharField(max_length=20, verbose_name='位置-左')
    loc_top = models.CharField(max_length=20, verbose_name='位置-上')
    size_width = models.CharField(max_length=20, verbose_name='图标宽', blank=True, null=True)
    size_height = models.CharField(max_length=20, verbose_name='图标高', blank=True, null=True)
    pause_image = models.ImageField(verbose_name='静止显示图片')
    video_file = models.FileField(verbose_name='视频文件')
    video_length = models.IntegerField(verbose_name='播放时长', blank=True, null=True)
    is_show = models.BooleanField(verbose_name='显示', default=True)

    class Meta:
        verbose_name = '视频元素'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



