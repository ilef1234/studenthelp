from django.shortcuts import render
from .forms import CommentForm, UserForm 
from .forms import PosteForm  # Importez le formulaire UserForm
from .forms import EvenementForm
from .forms import EvenClubForm
from .forms import EvenSocialForm
from .forms import StageForm
from .forms import LogementForm
from .forms import TransportForm
from .forms import RecommandationForm
from django.shortcuts import redirect
from .models import Poste, Reaction, Stage, User , EvenClub,EvenSocial
from .models import Evenement
from .models import Transport
from .models import Logement
from .models import Recommandation
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
# # Create your views here.
# def login(request):
#     return render(request,'login.html')

# @login_required
# def like_post(request):
#     if request.method == 'POST':
#         post_id = request.POST.get('post_id')
#         post = Poste.objects.get(id=post_id)
#         new_like = Reaction(poste=post, like=True)
#         new_like.save()
#         likes_count = post.count_likes()  # Mettre à jour le nombre de likes
#         return JsonResponse({'likes': likes_count})
#     else:
#         return JsonResponse({'error': 'Method not allowed'}, status=405)
def home(request):
   
    return render(request,'page0.html', {})
# def login(request):
#     error_message = None  # Initialisation du message d'erreur à None
#     if request.method == 'POST':
#         nom = request.POST.get('nom')
#         password = request.POST.get('password')
    
#         # Rechercher l'utilisateur dans la base de données en utilisant le téléphone ou l'email
#         # Utilisez la méthode `get()` pour rechercher par téléphone ou email
#         user = User.objects.filter(nom=nom).first()
#         if not user:
#             user = User.objects.filter(nom=nom).first()

#         # Vérifiez si l'utilisateur existe et si le mot de passe est correct
#         if user and user.password == password :
#             request.session['user_nom'] = user.nom

#             # Si l'utilisateur existe et le mot de passe est correct, redirigez vers la page de profil
#             # Remplacez 'profil' par le nom de votre URL de la page de profil
#             return redirect('profil')
#         else:
#             error_message = "User not found or invalid credentials"

#     # Rendre le template de connexion avec le message d'erreur
#     return render(request, 'login.html', {'error_message': error_message})
def login(request):
    error_message = None  # Initialisation du message d'erreur à None
    if request.method == 'POST':
        nom = request.POST.get('nom')
        password = request.POST.get('password')
    
        # Rechercher l'utilisateur dans la base de données en utilisant le nom
        user = User.objects.filter(nom=nom).first()

        # Vérifiez si l'utilisateur existe et si le mot de passe est correct
        if user and user.password == password :
            # Stocker le nom de l'utilisateur dans la session
            request.session['user_nom'] = user.nom

            # Rediriger vers la page de profil
            return redirect('profil')
        else:
            error_message = "User not found or invalid credentials"

    # Rendre le template de connexion avec le message d'erreur
    return render(request, 'login.html', {'error_message': error_message})

   
def user(request):
    if request.method == "POST": 
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Votre compte a été créé avec succès. Vous pouvez vous connecter maintenant !')
            return redirect('/Studenthelp')
    else:
        form = UserForm()  # Créer une instance du formulaire vide

    # Ajoutez le formulaire au contexte de la vue
    return render(request, 'majUser.html', {'form': form})

def poste(request):
    if request.method == "POST": 
        form = PosteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/Studenthelp/accueil/')
    else:
        form = PosteForm()  # Créer une instance du formulaire vide

    # Ajoutez le formulaire au contexte de la vue
    return render(request, 'majPoste.html', {'form': form})
def evenement(request):
    if request.method == "POST": 
        form = EvenementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/Studenthelp/accueil/')
    else:
        form = EvenementForm()  # Créer une instance du formulaire vide

    # Ajoutez le formulaire au contexte de la vue
    return render(request, 'majEvenement.html', {'form': form})
def evenementclub(request):
    if request.method == "POST": 
        form = EvenClubForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/Studenthelp/accueil/')
    else:
        form = EvenClubForm()  # Créer une instance du formulaire vide

    # Ajoutez le formulaire au contexte de la vue
    return render(request, 'majEvenclub.html', {'form': form})
def evenementsoc(request):
    if request.method == "POST": 
        form = EvenSocialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/Studenthelp/accueil/')
    else:
        form = EvenSocialForm()  # Créer une instance du formulaire vide

    # Ajoutez le formulaire au contexte de la vue
    return render(request, 'majEvensoc.html', {'form': form})
def stage(request):
    if request.method == "POST": 
        form = StageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/Studenthelp/accueil/')
    else:
        form = StageForm()  # Créer une instance du formulaire vide

    # Ajoutez le formulaire au contexte de la vue
    return render(request, 'majStage.html', {'form': form})
def logement(request):
    if request.method == "POST": 
        form = LogementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/Studenthelp/accueil/')
    else:
        form = LogementForm()  # Créer une instance du formulaire vide

    # Ajoutez le formulaire au contexte de la vue
    return render(request, 'majLog.html', {'form': form})
def transport(request):
    if request.method == "POST": 
        form = TransportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/Studenthelp/accueil/')
    else:
        form = TransportForm()  # Créer une instance du formulaire vide

    # Ajoutez le formulaire au contexte de la vue
    return render(request, 'majTransp.html', {'form': form})

def recommandation(request):
    if request.method == "POST": 
        form = RecommandationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/Studenthelp/accueil/')
    else:
        form = RecommandationForm()  # Créer une instance du formulaire vide

    # Ajoutez le formulaire au contexte de la vue
    return render(request, 'majRec.html', {'form': form})

def accueil(request):
    if request.session.get('user_nom'):
        postes = Poste.objects.order_by('-date')
        context = {'postes': postes}
        return render(request, 'accueil.html', context)
    else:
        return redirect('http://127.0.0.1:8000/Studenthelp/login/')

#     items = []

#     stages = Stage.objects.all()
#     logements = Logement.objects.all()
#     evenements = Evenement.objects.all()
#     transports = Transport.objects.all()
#     recommandations = Recommandation.objects.all()

#     for stage in stages:
#         stage.type = "Stage"
#         items.append(stage)

#     for logement in logements:
#         logement.type = "Logement"
#         items.append(logement)

#     for evenement in evenements:
#         evenement.type = "Evenement"
#         items.append(evenement)

#     for transport in transports:
#         transport.type = "Transport"
#         items.append(transport)

#     for recommandation in recommandations:
#         recommandation.type = "Recommandation"
#         items.append(recommandation)
#     if not items:
#         message = "No items found."  # Message to display if items list is empty
#     else:
#         message = None

#     return render(request, 'accueil.html', {'items': items, 'message': message})

def profil(request):
    if request.session.get('user_nom'):
        user_nom = request.session['user_nom']
        user = User.objects.filter(nom=user_nom).first()

        context = {
            'poste': Poste.objects.filter(user=user).order_by('-date'),  # Filtrer les publications de l'utilisateur connecté
            'reactions': Reaction.objects.all(),
            'user_nom': user_nom,
        }
        return render(request, 'profil.html', context)
    else:
        return redirect('http://127.0.0.1:8000/Studenthelp/login/')

# def home2(request):
#     context = {
#         'poste': Poste.objects.all(),
#         'reactions': Reaction.objects.all(),
#     }
#     return render(request, 'blog/home.html', context)
# def register(request):
#     if request.method == 'POST' :
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request,user)
#             messages.success(request, f'Coucou {username}, Votre compte a été
#             créé avec succès !')
#             return redirect('home')
#     else :
#         form = UserForm()
#     return render(request,'profil0.html',{'form' : form})

def logout_view(request): 
  logout(request)
  return redirect('/Studenthelp/')
class ListePost(ListView):
    model = Poste
    template_name = 'liste_postes.html'
    context_object_name = 'postes'
class DetailPost(DetailView):
    model = Poste
    template_name = 'detail_post.html'
    context_object_name = 'post'
class CreerPost(CreateView):
    model = Poste
    template_name = 'creer_post.html'
    form_class = PosteForm 
    success_url = reverse_lazy('profil') 
class ModifierPost(UpdateView):
    model = Poste
    template_name = 'modifier_post.html'
    form_class = PosteForm 
    success_url = reverse_lazy('profil') 
    # class ModifierPost(UpdateView):
    # model = Poste
    # template_name = 'modifier_post.html'
    # form_class = PosteForm 

    # # Redirection conditionnelle
    # def get_success_url(self):
    #     # Vérifie si la page précédente est le profil
    #     if self.request.META.get('HTTP_REFERER') == reverse_lazy('profil'):
    #         return reverse_lazy('profil')
    #     # Sinon, redirige vers l'accueil
    #     return reverse_lazy('accueil')

class SupprimerPost(DeleteView):
    model = Poste
    template_name = 'supprimer_post.html'
    success_url = reverse_lazy('profil') 
# class SupprimerPost(DeleteView):
#     model = Poste
#     template_name = 'supprimer_post.html'

#     # Redirection conditionnelle
#     def get_success_url(self):
#         # Vérifie si la page précédente est le profil
#         if self.request.META.get('HTTP_REFERER') == reverse_lazy('profil'):
#             return reverse_lazy('profil')
#         # Sinon, redirige vers l'accueil
#         return reverse_lazy('accueil')

def choix(request):
    return render(request, 'choix.html')

def contact(request):
    return render(request, 'contact.html')
  

def combined_view(request):
    evenement= Evenement.objects.all()
    stages = Stage.objects.all()
    logements = Logement.objects.all()
    transports = Transport.objects.all()
    recommandations = Recommandation.objects.all
    evenementsoc= EvenSocial.objects.all()
    evenementclub=EvenClub.objects.all()

    context = {
        'evenement': evenement,
        'stages': stages,
        'logements': logements,
        'transports': transports,
        'recommandations': recommandations,
        'evenementsoc':evenementsoc,
        'evenementclub':evenementclub
    }

    return render(request, 'combined_view.html', context)
# from django.shortcuts import get_object_or_404
# from django.contrib.auth.mixins import LoginRequiredMixin


# from django.contrib.auth import get_user_model

# User = get_user_model()

# class Addcomment(LoginRequiredMixin, CreateView):
#     model = Reaction
#     form_class = CommentForm
#     template_name = 'Addcmn.html'

#     def form_valid(self, form):
#         try:
#             username = self.request.session['user_nom']
#             form.instance.user = username
#             # Get the post object using the pk from the URL
#             post_pk = self.kwargs['pk']
#             post = get_object_or_404(Poste, pk=post_pk)
#             # Set the poste field to the retrieved post object
#             form.instance.poste = post
#             return super().form_valid(form)
#         except Exception as e:
#             print("Error occurred:", e)
#             return super().form_invalid(form)

#     success_url = reverse_lazy('accueil')

class Addcomment(CreateView):
    model = Reaction
    form_class = CommentForm
    template_name = 'Addcmn.html'

    def form_valid(self, form):
        default_user = User.objects.get(nom='ilef')
        form.instance.users = default_user
        form.instance.post_id = self.kwargs.get('pk')
        
        return super().form_valid(form)

    success_url = reverse_lazy('accueil')

