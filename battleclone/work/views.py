from django.views.generic import FormView, DetailView
from .forms import WorkModelForm
from battleclone.account.models import UserProfile
from .models import Work


class WorkView(FormView):
    template_name = 'work/work_view.html'
    success_url = '/work'
    form_class = WorkModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['object'] = UserProfile.objects.get(user=user)

        try:
            context['work_object'] = (Work.objects
                                          .filter(character__userprofile__user=user)
                                          .latest('started'))
        except Work.DoesNotExist as e:
            print("Does not exist")

        # TODO: add return work object -> maybe add new inheritance ? formview with detail view
        return context

    def post(self, request, *args, **kwargs):
        form = WorkModelForm(request.POST)
        if form.is_valid():
            character = UserProfile.objects.get(user=self.request.user).character

            instance = form.save(commit=False)
            instance.character = character
            instance.save()

            character.update_status('WORK')

        return super().post(request, *args, **kwargs)


def finish_work(request):
    pass


# TODO: login required
# TODO: work detail view
# TODO: work list view
# TODO: work table?
