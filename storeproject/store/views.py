from django.http import HttpResponse
from store.models import Creator

def home(request):
    return HttpResponse('Привіт це мій перший views!')

def creators(request):
    creators_obj = Creator.objects.all()
    return HttpResponse(creators_obj)

def creator(request, pk):
    creators_obj = Creator.objects.filter(id=pk)
    return HttpResponse(creators_obj)