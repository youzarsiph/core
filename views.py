""" ViewSets """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from core_lms.models import User, Program, Course, Week, Section, Lesson
from core_lms.serializers import (
    UserSerializer, ProgramSerializer, CourseSerializer,
    WeekSerializer, SectionSerializer, LessonSerializer
)


class ViewSet(ModelViewSet):
    """ ViewSet """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    search_fields = []
    ordering_fields = []

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """

        if self.action in ('list', 'retrieve'):
            permission_classes = [IsAuthenticated]

        else:
            permission_classes = [IsAuthenticated, IsAdminUser]

        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        """ Add the user field """

        serializer.save(user=self.request.user)


class UserViewSet(ModelViewSet):
    """ User ViewSet """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    search_fields = []
    ordering_fields = []


class ProgramViewSet(ModelViewSet):
    """ Program ViewSet """

    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    search_fields = []
    ordering_fields = []


class CourseViewSet(ModelViewSet):
    """ Course ViewSet """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    search_fields = []
    ordering_fields = []


class WeekViewSet(ModelViewSet):
    """ Week ViewSet """

    queryset = Week.objects.all()
    serializer_class = WeekSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    search_fields = []
    ordering_fields = []


class SectionViewSet(ModelViewSet):
    """ Section ViewSet """

    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    search_fields = []
    ordering_fields = []


class LessonViewSet(ModelViewSet):
    """ Lesson ViewSet """

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    search_fields = []
    ordering_fields = []
