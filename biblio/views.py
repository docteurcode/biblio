from django.shortcuts import render
from django.views import View
from biblio.models import Cours, Ebook, Personne


class EbookView(View):
    def get(self, request):
        donnee = Ebook.objects.all()[:12]
        return render(request, "pages/livres.html", {'data':donnee})
    
    def post(self, request):
        post = request.POST
        livres = Ebook.objects.filter(titre__contains=post.get('search'))
        data= {
            'type':'livre',
            'data':livres,
            'search' : post.get('search')
        }
        return render(request, "pages/recherche.html", data)


class CoursView(View):
    def get(self, request):
        donnee = Cours.objects.all()[:12]
        return render(request, "pages/videos.html", {'data':donnee})
    
    def post(self, request):
        post = request.POST
        cours = Cours.objects.filter(titre__contains=post.get('search'))
        data= {
            'type':'cours',
            'data':cours,
            'search' : post.get('search')
        }
        return render(request, "pages/recherche.html", data)


class Result(View):
    def get(self, request): 
        return render(request)
    


class LecteurPDF(View):
    def get(self, request, key): 
        item = Ebook.objects.get(keydata=key)
        item.lecturePlus()
        item.save()
        return render(request, 'pages/lecteurPDF.html', {'data':item})
    

class LecteurVideo(View):
    def get(self, request, key): 
        item = Cours.objects.get(keydata=key)
        item.lecturePlus()
        item.save()
        return render(request, 'pages/lecteurVideos.html', {'data':item})
    

class DetailsPageEbook(View):
    def get(self, request, key):
        item = Ebook.objects.get(keydata=key) 
        data = {
            'data' : item,
            'recommandation' : Ebook.objects.filter(classe=item.classe).exclude(keydata=item.keydata),
        }
        return render(request, 'pages/details.html', data)
    

class DetailsPageVideo(View):
    def get(self, request, key):
        item = Cours.objects.get(keydata=key) 
        data = {
            'data' : item,
            'recommandation' : Cours.objects.filter(classe=item.classe).exclude(keydata=item.keydata),
        }
        return render(request, 'pages/detailsV.html', data)
    