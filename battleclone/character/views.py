from django.shortcuts import render
from django.views.generic import TemplateView
from battleclone.account.models import UserProfile
from .models import Parameters


class CharacterView(TemplateView):
    template_name = "character.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['character_attributes'] = Parameters.objects.get(id=1)
    #     context['object'] = UserProfile.objects.get(user=self.request.user)
    #     return context
