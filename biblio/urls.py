from django.urls import path
from biblio.views import CoursView, DetailsPageEbook, DetailsPageVideo, EbookView, LecteurPDF, LecteurVideo
from .api import EbookViewAPi, VideoViewApi

urlpatterns = [
    path("", EbookView.as_view(), name='homepage'),
    path("cours-videos/", CoursView.as_view(), name='videos'),
    path("livre/<key>/", DetailsPageEbook.as_view(), name='detailsE'),
    path("cours-video/<key>/", DetailsPageVideo.as_view(), name='detailsV'),
    path("lecture/ebook/<key>/", LecteurPDF.as_view(), name='lecteurPDF'),
    path("lecture/cours-videos/<key>/", LecteurVideo.as_view(), name='lecteurVideo'),
    
    path("api/ebook", EbookViewAPi.as_view()),
    path("api/video", VideoViewApi.as_view()),
]

