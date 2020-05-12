from django.shortcuts import get_object_or_404, render

from .models import SoundMap

# Create your views here.


def show_map(request, map_id):
    sound_map = get_object_or_404(SoundMap, pk=map_id)
    context = {'sound_map': sound_map}
    return render(request, 'view_map.html', context)
