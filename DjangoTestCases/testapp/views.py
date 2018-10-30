from django.shortcuts import render

from .models import Band
# Create your views here.


def index(request):
    bands = Band.objects.all()
    context = {'bands' : bands}
    return render(request, 'testapp/index.html', context)