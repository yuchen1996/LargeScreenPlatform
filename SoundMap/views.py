from django.shortcuts import get_object_or_404, render

from .models import SoundMap

# Create your views here.


def show_map(request, map_id):
    map = get_object_or_404(SoundMap, pk=map_id)
    context = {'map': map}
    return render(request, 'show_map.html', context)
