
from django.http import HttpResponse
from django.shortcuts import render_to_response
import os

def default(request):
        if request.META.get('HTTP_ACCEPT_LANGUAGE') and 'ru-RU' in request.META.get('HTTP_ACCEPT_LANGUAGE'):
                lang = 'ru'
        else:
                lang = 'en'
        ddir = os.getcwd()
        return render_to_response('default.html', {'lang': lang, 'ddir': ddir})
