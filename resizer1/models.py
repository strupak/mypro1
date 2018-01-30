# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Article(models.Model):
    
    article_title = models.CharField(max_length=200)
    article_content = models.CharField(max_length=300)
    img = models.ImageField(upload_to='resizer1/static/resizer1/images/')
    def __str__(self):
        return self.article_title
        
