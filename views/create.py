from core_lms.models import *
from core_lms.forms.create import *
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from core_lms.views.generic import CreationView, MessageRequiredCreationView
from core_lms.views.mixins import LoginRequiredMixin

User = get_user_model()


class UserCreationView(CreationView):
    model = User
    form_class = StyledUserCreationForm
    success_url = reverse_lazy('core_lms:login')

    def get_success_url(self):
        return reverse_lazy('core_lms:edit_user', args=[self.object.pk])


class CourseCreationView(LoginRequiredMixin, MessageRequiredCreationView):
    model = Course
    form_class = CourseCreationForm
    success_url = reverse_lazy('core_lms:index')
