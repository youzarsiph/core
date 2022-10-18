from core_lms.models import *
from django.urls import reverse_lazy
from django.contrib.auth.views import get_user_model
from core_lms.views.generic import MessageRequiredDeletionView, RequestUser, LoginRequiredMixin, AuthorityRequiredMixin

User = get_user_model()


class UserDeletionView(LoginRequiredMixin, RequestUser, MessageRequiredDeletionView):
    model = User
    success_url = reverse_lazy('core_lms:index')
    success_message = 'Account deleted successfully.'
    error_message = 'Error occurred while processing.'


class ProgramDeletionView(AuthorityRequiredMixin, MessageRequiredDeletionView):
    model = Program
    success_url = reverse_lazy('core_lms:program_list')


class CourseDeletionView(AuthorityRequiredMixin, MessageRequiredDeletionView):
    model = Course
    success_url = reverse_lazy('core_lms:course_list')
