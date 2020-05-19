from django.shortcuts import get_object_or_404, render

from .models import SoundMap, Image, Audio, Video


# Create your views here.


def show_map(request, map_id):
    sound_map = get_object_or_404(SoundMap, pk=map_id)
    images = Image.objects.filter(map_id=map_id)
    audios = Audio.objects.filter(map_id=map_id)
    videos = Video.objects.filter(map_id=map_id)
    context = {
        'sound_map': sound_map,
        'images': images,
        'audios': audios,
        'videos': videos,
    }
    return render(request, 'view_map.html', context)
