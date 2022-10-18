from core_lms.models import *
from django.contrib import messages
from django.urls import reverse_lazy
from core_lms.forms.main import UserEditForm, ProgramCreationForm, CourseCreationForm
from django.contrib.auth.views import get_user_model
from core_lms.views.generic import MessageRequiredEditView, RequestUser, LoginRequiredMixin, AuthorityRequiredMixin

User = get_user_model()


class UserEditView(LoginRequiredMixin, RequestUser, MessageRequiredEditView):
    model = User
    form_class = UserEditForm
    success_url = reverse_lazy('core_lms:profile')
    success_message = 'Account updated successfully.'
    error_message = 'Error occurred while processing.'

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        if not (user.first_name and user.last_name and user.email):
            messages.success(request, 'Thanks for signing up, please complete yor profile')
        return super().get(request, *args, **kwargs)


class ProgramEditView(AuthorityRequiredMixin, MessageRequiredEditView):
    model = Program
    form_class = ProgramCreationForm
    success_url = reverse_lazy('core_lms:program_list')


class CourseEditView(AuthorityRequiredMixin, MessageRequiredEditView):
    model = Course
    form_class = CourseCreationForm
    success_url = reverse_lazy('core_lms:dashboard')
