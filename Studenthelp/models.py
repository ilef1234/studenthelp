from django.db import models
from datetime import date
# Create your models here.
class User(models.Model):
    nom=models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    telephone=models.CharField(max_length=100)
    email=models.EmailField(default='Non definie')
    password=models.CharField(max_length=100 ,default="Enter your password")
   

  

    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"
    def __str__(self) :
        return str(self.nom) 

class Poste(models.Model):
    TYPE_CHOICES = [( 0,"offre"), ( 1,"demande")]
    image = models.ImageField(blank=True)
    type = models.IntegerField(choices=TYPE_CHOICES,default="0")
    date = models.DateField(null=True, default=date.today) 
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    def affichertype(self):
          return 'offre' if self.type == 0 else 'demande'
    def count_likes(self):
        # Récupérer les réactions associées à ce poste
        reactions = Reaction.objects.filter(poste=self, like=True)
        # Compter le nombre de réactions
        return reactions.count()
   

    def __str__(self) :
        return str(self.image)+" "+str(self.type)+" "+str(self.date)+" "+str(self.user)
class Reaction(models.Model):
    comment=models.TextField(default='Non definie')
    like=models.BooleanField()
    user=models.ForeignKey('User',on_delete=models.CASCADE,null=True)
    poste=models.ForeignKey('Poste',on_delete=models.CASCADE,null=True)
    def __str__(self) :
        return str(self.comment) +" "+str(self.like)+" "+str(self.user)+" "+str(self.poste)
    
class Evenement (Poste,models.Model):
    intitule=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    lieu=models.CharField(max_length=100)
    contactinfo=models.CharField(max_length=100)
    def __str__(self):
      return super().__str__() + str(self.intitule)+" "+str(self.description)+" "+str(self.lieu)+" "+str(self.contactinfo)
class EvenClub(Evenement,models.Model):
    club=models.CharField(max_length=100)
    def __str__(self):
      return super().__str__() + str(self.club)
class EvenSocial(Evenement,models.Model):
    prix=models.FloatField()
    def __str__(self):
      return super().__str__() + str(self.prix)

class Stage(Poste,models.Model):
    TYPE_CHOICES=[(1,"ouvrier"),(2,"tachnicien"),(3,"PFE")] 
    typestg=models.IntegerField(choices=TYPE_CHOICES)
    societe=models.CharField(max_length=100)
    duree=models.CharField(max_length=100,default="")
    sujet=models.CharField(max_length=100)
    contactinfo=models.CharField(max_length=100)
    specialite=models.CharField(max_length=100)
    def __str__(self):
      return super().__str__() + str(self.typestg) + " " + str(self.societe) + " " + str(self.duree) + " " + str(self.sujet) + " " + str(self.contactinfo) + " " + str(self.specialite)

class Logement(Poste,models.Model):
    localisation=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    contactinfo=models.CharField(max_length=100)
    def __str__(self):
      return super().__str__() + str(self.localisation)+" "+str(self.description)+" "+str(self.contactinfo)
class Transport(Poste,models.Model):
    depart=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    heuredep=models.TimeField()
    nbsiege=models.IntegerField()
    contactinfo=models.CharField(max_length=100)
    def __str__(self):
      return super().__str__() + str(self.depart)+" "+str(self.destination)+" "+str(self.heuredep)+" "+str(self.nbsiege)+" "+str(self.contactinfo)
class Recommandation(Poste,models.Model):
    text=models.CharField(max_length=100)
    def __str__(self):
      return super().__str__() + str(self.text)


