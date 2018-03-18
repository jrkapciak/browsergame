from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth.decorators import login_required

# Create your views here.

class WorkView(FormView):



    def get_success_url(self):
        pass


