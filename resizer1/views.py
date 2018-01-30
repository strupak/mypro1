# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render_to_response, get_object_or_404
from .models import *
# Create your views here.

class EArticleView(View):
    template_name = 'resizer1/index.html'
    
    def get(self, request, *args, **kwargs):
        context = {}
        article = get_object_or_404(Article, pk=1)
        context['article'] = article
        return render_to_response(template_name=self.template_name, context=context)
        
    def image(request):
        images = Article.objects.all()# тут objects
        return render(request, 'resizer1/index.html',{'images':images})