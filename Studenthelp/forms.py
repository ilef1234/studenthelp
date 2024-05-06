from django.forms import ModelForm
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
class UserForm(ModelForm):
    class Meta :
        model = User
        fields = "__all__"

class ReactionForm(ModelForm):
    class Meta:
      model = Reaction
      fields = "__all__"

class PosteForm(ModelForm):
    class Meta:
        model= Poste
        fields = "__all__"
class EvenementForm(ModelForm):
    class Meta:
        model= Evenement
        fields = "__all__"
class EvenClubForm(ModelForm):
    class Meta:
        model= EvenClub
        fields = "__all__"
class EvenSocialForm(ModelForm):
    class Meta:
        model= EvenSocial
        fields = "__all__"
class StageForm(ModelForm):
    class Meta:
        model= Stage
        fields = "__all__"
class LogementForm(ModelForm):
    class Meta:
        model= Logement
        fields = "__all__"
class TransportForm(ModelForm):
    class Meta:
        model= Transport
        fields = "__all__"
class RecommandationForm(ModelForm):
    class Meta:
        model= Recommandation
        fields = "__all__"