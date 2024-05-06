from django.contrib import admin

# Register your models here.
from .models import User
from .models import Reaction
from .models import Poste
from .models import Evenement
from .models import EvenClub
from .models import EvenSocial
from .models import Stage
from .models import Logement
from .models import Transport
from .models import Recommandation
admin.site.register(User)
admin.site.register(Reaction)
admin.site.register(Poste)
admin.site.register(Evenement)
admin.site.register(EvenClub)
admin.site.register(EvenSocial)
admin.site.register(Stage)
admin.site.register(Logement)
admin.site.register(Transport)
admin.site.register(Recommandation)