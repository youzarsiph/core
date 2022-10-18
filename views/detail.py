from core_lms.models import *
from core_lms.views.generic import DetailsView


class CourseDetailView(DetailsView):
    model = Course
    # slug_field = 'title'
