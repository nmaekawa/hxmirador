
import logging
from urllib.parse import urlparse

from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt

from hxlti.decorators import require_lti_launch

@csrf_exempt
@xframe_options_exempt  # allows rendering in Canvas|edx frame
@require_lti_launch
def lti_mirador(request):
    # get list of manifests
    manifests_ids = request.POST.get('custom_manifests', '')
    manifests = manifests_ids.split(';') if manifests_ids else []

    # mirador options
    layout = request.POST.get('custom_layout', '1x1')

    # window specific parameters
    view_type = request.POST.get('custom_view_type', 'ImageView')

    # canvases
    canvas_ids = request.POST.get('canvases', None)
    canvases = canvas_ids.split(';') if canvas_ids else []

    # map manifests to canvases
    manifest_canvas_map = {}
    for m in manifests:
        found_canvas = False
        for canvas in canvases:
            if m in canvas:
                manifest_canvas_map[m] = canvas.replace(' ', '')
                found_canvas = True
        if not found_canvas:
            manifest_canvas_map[m] = ''

    return render(
        request, 'mirador/mirador_instance.html', {
            'manifests': manifests,
            'layout': layout,
            'view_type': view_type,
            'manifest_canvas_map': manifest_canvas_map,

        })




