from core_lms.models import *
from core_lms.views.generic import ListingView
from core_lms.views.mixins import AuthorityRequiredMixin


class ProgramListView(AuthorityRequiredMixin, ListingView):
    model = Program


class CourseListView(AuthorityRequiredMixin, ListingView):
    model = Course
