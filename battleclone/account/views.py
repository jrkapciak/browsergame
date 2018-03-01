from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from .forms import SignUpForm


# Create your views here.


class RegistrationView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = '/login'

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated():
            # TODO: need to create return redirect to homepage or somf
            return HttpResponseForbidden()

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()

        return super().form_valid(form)



