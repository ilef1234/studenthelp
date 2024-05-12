from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import ListePost, DetailPost, CreerPost, ModifierPost, SupprimerPost
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name='login'),
    path('user/', views.user, name='user'),
    path('accueil/', views.accueil, name='accueil'),
    path('poste/', views.poste, name='poste'),
    path('evenement/', views.evenement, name='evenement'),
    path('evenementclub/', views.evenementclub, name='evenementclub'),
    path('evenementsoc/', views.evenementsoc, name='evenementsoc'),
    path('stage/', views.stage, name='stage'),
    path('logement/', views.logement, name='logement'),
    path('transport/', views.transport, name='transport'),
    path('recommandation/', views.recommandation, name='recommandation'),
    path('profil/', views.profil, name="profil"),
    path('', ListePost.as_view(), name='liste_postes'),  # Utilisation des vues génériques basées sur les classes
    path('detail_post/<int:pk>/', DetailPost.as_view(), name='detail_post'),
    path('creer_post/', CreerPost.as_view(), name='creer_post'),
   path('modifier_post/<int:pk>/', ModifierPost.as_view(), name='modifier_post'),

    path('supprimer_post/<int:pk>/', SupprimerPost.as_view(), name='supprimer_post'),
    path('choix/', views.choix, name="choix"),
    path('contact/', views.contact, name="contact"),
]

# Définir l'URL pour les fichiers média en mode DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
