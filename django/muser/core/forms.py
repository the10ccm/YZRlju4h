from django.forms import ModelForm, inlineformset_factory
from django.contrib.auth import get_user_model

from .models import CustomUser


class CustomUserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['birthday', 'bizzfuzz_number']

CustomUserFormSet = inlineformset_factory(
    get_user_model(), CustomUser, fields=('birthday', 'bizzfuzz_number'),
    can_delete=False)
