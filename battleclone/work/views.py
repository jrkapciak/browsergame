from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth.decorators import login_required
from .forms import WorkModelForm
from battleclone.account.models import UserProfile


class WorkView(FormView):
    template_name = 'work/work_view.html'
    form_class = WorkModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = UserProfile.objects.get(user=self.request.user)
        return context
