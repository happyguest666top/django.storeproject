from django.http import HttpResponse
from store.models import Creator
from django.shortcuts import render


def home(request):
    #return HttpResponse('Привіт це мій перший views!')
    return render(request, 'home.html')

def creators(request):
    creators_obj = Creator.objects.all()
    #return HttpResponse(creators_obj)
    context = {'creators': creators_obj}
    return render(request, 'creators.html', context)

def creator(request, pk):
    creators_obj = Creator.objects.filter(id=pk)
    #return HttpResponse(creators_obj)
    context = {'creator': creators_obj}
    return render(request, 'creator.html', context)