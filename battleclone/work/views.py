from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth.decorators import login_required
from .forms import WorkModelForm


class WorkView(FormView):
    template_name = 'work/work_view.html'
    form_class = WorkModelForm




