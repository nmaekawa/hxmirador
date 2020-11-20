import logging

from django.conf import settings


def unpack_custom_parameters(post_params):
    request_params = {}
    pmap = settings.HXMIRADOR_CUSTOM_PARAMETERS_MAP

    for key in pmap:
        pvalue = post_params.get(key, "").strip()

        if pvalue:
            if pmap[key]["ptype"] == "list":
                if pvalue:
                    value = [x.strip() for x in pvalue.split(";")]
                else:
                    value = []
            else:
                value = pvalue
            request_params[pmap[key]["mapto"]] = value

    return request_params
