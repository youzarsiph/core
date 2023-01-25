""" URLConf """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core_lms.views import (
    UserViewSet, ProgramViewSet, CourseViewSet,
    WeekViewSet, SectionViewSet, LessonViewSet
)


# Define the router to register the viewsets
router = DefaultRouter(trailing_slash=False)

router.register('users', UserViewSet, 'user')
router.register('programs', ProgramViewSet, 'program')
router.register('courses', CourseViewSet, 'course')
router.register('weeks', WeekViewSet, 'week')
router.register('sections', SectionViewSet, 'section')
router.register('lessons', LessonViewSet, 'lesson')


app_name = 'core_lms'

urlpatterns = [
    path('api/', include(router.urls))
]
