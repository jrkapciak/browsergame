from django.http import HttpResponseForbidden
from django.shortcuts import reverse
from django.views.generic import CreateView, UpdateView
from .forms import SignUpForm
from .models import UserProfile
from battleclone.character.models import Character, Parameters


class RegistrationView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = '/login'

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated():
            # TODO: need to create return redirect to homepage or somf
            return HttpResponseForbidden()

        return super().dispatch(request, *args, **kwargs)

    @classmethod
    def create_character(cls, new_user):
        parameters = Parameters.objects.create()

        return Character.objects.create(
            nickname=new_user.username, parameters=parameters
        )

    @classmethod
    def create_profile(cls, new_user, new_character):
        UserProfile.objects.create(
            user=new_user, character=new_character
        )

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()

        new_character = self.create_character(new_user)

        self.create_profile(new_user, new_character)

        return super().form_valid(form)


class EditProfileView(UpdateView):
    model = UserProfile
    fields = ('description', 'avatar',)
    template_name = 'profile/edit_profile.html'
    slug_field = 'pk'

    def get_success_url(self):
        return reverse('edit_profile', kwargs=dict(pk=self.get_object().pk))


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        print(context)

        return  context