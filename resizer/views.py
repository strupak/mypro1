from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse

from resizer.models import Document
from resizer.forms import DocumentForm

from django.views import View
from django.shortcuts import render_to_response, get_object_or_404
from .models import *

def upload(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('resizer:index'))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    # Render list page with the documents and the form
    return render(
        request,
        'resizer/upload.html',
        {'form': form}
    )

def index(request):
    wer = Document.objects.all()
    return render(request,'resizer/index.html', {'wer': wer})