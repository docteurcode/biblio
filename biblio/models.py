from django.db import models
import uuid

class Data(models.Model):
    CHOICES = (
        ('Seconde A', 'Seconde A'),
        ('Seconde S', 'Seconde S'),
        ('Permiere A', 'Premiere A'),
        ('Permiere S', 'Premiere S'),
        ('Terminale A', 'Terminale A'),
        ('Terminale S', 'Terminale S'),
    )
    titre = models.CharField(max_length=100, verbose_name="Titre", unique=True)
    description = models.TextField(verbose_name="Description", default="Aucune description", blank=True)
    date   = models.DateField(auto_now=True, verbose_name="Date de mise en ligne")
    date_up   = models.DateField(auto_now_add=True, verbose_name="Date de mise à jours")
    keydata = models.UUIDField(editable=False)
    classe = models.CharField(max_length=100, choices=CHOICES, verbose_name="Choisissez une classe")
    nombre_de_lecture = models.IntegerField(default=0, editable=False)
    
    class meta:
        abstract = True
    
    def lecturePlus(self):
        self.nombre_de_lecture +=1
        self.save()
        
    def __str__(self) -> str:
        return self.titre + ' / ' + self.classe
    
    def save(self, *args,**kwargs):
        if not self.id:
            self.keydata = uuid.uuid1()
            
        super().save(*args, **kwargs)
        
class Ebook(Data):
    file = models.FileField(upload_to="Ebook/%d-%M-%Y", verbose_name="Fichier (PDF, EBOOK)")
    
    
class Cours(Data):
    file = models.FileField(upload_to="Cours/%d-%M-%Y", verbose_name="Fichier (Vidéo)")
    



class Personne(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)