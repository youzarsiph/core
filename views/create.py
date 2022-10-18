from core_lms.models import *
from core_lms.forms.create import *
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from core_lms.views.mixins import UserRequiredMixin
from core_lms.views.generic import CreationView, MessageRequiredCreationView

User = get_user_model()


class SelfRedirect:
    """
    A mixin to customize success_url of Create or Update views
    """
    # view attribute can only be 'create' or 'edit'
    view: str = 'edit'

    def get_success_url(self):
        model_name = self.model._meta.verbose_name.title().lower()
        pattern = f'core_lms:{self.view}_{model_name}'
        return reverse_lazy(pattern, args=[self.object.pk])


class UserCreationView(CreationView):
    model = User
    form_class = StyledUserCreationForm
    success_url = reverse_lazy('core_lms:login')

    def get_success_url(self):
        return reverse_lazy('core_lms:edit_user', args=[self.object.pk])


class ProgramCreationView(SelfRedirect, UserRequiredMixin, MessageRequiredCreationView):
    model = Program
    form_class = ProgramCreationForm


class CourseCreationView(SelfRedirect, UserRequiredMixin, MessageRequiredCreationView):
    model = Course
    form_class = CourseCreationForm
