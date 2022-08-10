from core_lms.views.list import *
from core_lms.views.edit import *
from core_lms.views.create import *
from core_lms.views.detail import *
from core_lms.views.delete import *
from django.views.generic import TemplateView
from core_lms.views.mixins import DashboardMixin, LoginRequiredMixin


# Create your views here.
class IndexView(TemplateView):
    template_name = 'core_lms/base/index.html'


class AboutView(TemplateView):
    template_name = 'core_lms/base/about.html'


class ContactView(TemplateView):
    template_name = 'core_lms/base/contact.html'


class DashboardView(DashboardMixin, TemplateView):
    template_name = 'core_lms/base/dashboard.html'
    permission_required = 'JApp.view_example'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'core_lms/authentication/profile.html'
