from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import render, reverse
from django.views.generic import CreateView, UpdateView
from .forms import SignUpForm
from .models import UserProfile


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


class EditProfileView(UpdateView):
    model = UserProfile
    fields = ('description', 'avatar',)
    template_name = 'profile/edit_profile.html'
    slug_field = 'pk'

    def get_success_url(self):
        return reverse('edit_profile', kwargs=dict(pk=self.get_object().pk))




