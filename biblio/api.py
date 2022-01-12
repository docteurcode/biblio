from django.views import View
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from .models import Cours, Ebook


class EbookViewAPi(View):
    def get(self, request):
        data = [
            {'titre' : item.titre,
             'description' : item.description,
             'date' : item.date.strftime('%d %b %Y'),
             'classe' : item.classe,
             'fichier' : request.get_host()+item.file.url,
             } for item in  Ebook.objects.all()
            ] 
        # data  = serializers.serialize('json', data)
        # return HttpResponse(data, content_type="application/json")
        return JsonResponse(data, safe=False) 


class VideoViewApi(View):
    def get(self, request):
        data = [
            {'titre' : item.titre,
             'description' : item.description,
             'date' : item.date.strftime('%d %b %Y'),
            #  'date' : f'{item.date.day}/{item.date.month}/{item.date.year}',
             'classe' : item.classe,
             'fichier' : request.get_host()+item.file.url,
             } for item in  Ebook.objects.all()
            ] 
        return HttpResponse(data, content_type="application/json")