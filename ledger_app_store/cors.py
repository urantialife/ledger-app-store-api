import re

from django import http
from django.apps import apps
from django.utils.cache import patch_vary_headers
from django.utils.six.moves.urllib.parse import urlparse
from django.utils.deprecation import MiddlewareMixin

ACCESS_CONTROL_ALLOW_ORIGIN = 'Access-Control-Allow-Origin'
ACCESS_CONTROL_EXPOSE_HEADERS = 'Access-Control-Expose-Headers'
ACCESS_CONTROL_ALLOW_CREDENTIALS = 'Access-Control-Allow-Credentials'
ACCESS_CONTROL_ALLOW_HEADERS = 'Access-Control-Allow-Headers'
ACCESS_CONTROL_ALLOW_METHODS = 'Access-Control-Allow-Methods'
ACCESS_CONTROL_MAX_AGE = 'Access-Control-Max-Age'
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'DELETE'
]

class CorsMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        """
        Add the respective CORS headers
        """
        patch_vary_headers(response, ['Origin'])

        origin = request.META.get('HTTP_ORIGIN')
        response[ACCESS_CONTROL_ALLOW_ORIGIN] = origin
        response[ACCESS_CONTROL_ALLOW_HEADERS] = ', '.join(CORS_ALLOW_HEADERS)
        response[ACCESS_CONTROL_ALLOW_METHODS] = ', '.join(CORS_ALLOW_METHODS)

        return response
