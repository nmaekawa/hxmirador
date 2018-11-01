
import logging
from urllib.parse import urlparse

from django.conf import settings
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt

from hxlti.decorators import require_lti_launch
from mirador.util import unpack_custom_parameters

@csrf_exempt
@xframe_options_exempt  # allows rendering in Canvas|edx frame
@require_lti_launch
def lti_mirador(request):

    # get lti params from request
    lti_params = unpack_custom_parameters(request.POST)

    # mirador options
    layout = lti_params.get('layout', '1x1')

    # window specific parameters
    view_type = lti_params.get('view_type', 'ImageView')

    # canvases
    canvases = lti_params.get('canvases', [])

    # manifests
    manifests = lti_params.get('manifests', [])

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

    logger = logging.getLogger(__name__)
    logger.debug(
        'manifests({}), layout({}), view_type({}), canvas_map({})'.format(
            manifests, layout, view_type, manifest_canvas_map))

    return render(
        request, 'mirador/mirador_instance.html', {
            'manifests': manifests,
            'layout': layout,
            'view_type': view_type,
            'manifest_canvas_map': manifest_canvas_map,

        })





