""" Data Serialization """


from rest_framework.serializers import HyperlinkedModelSerializer
from core_lms.models import User, Program, Course, Week, Section, Lecture


class UserSerializer(HyperlinkedModelSerializer):
    """ User Serializer """

    class Meta:
        """ Meta Data """

        model = User
        fields = ['id', 'url', ]


class ProgramSerializer(HyperlinkedModelSerializer):
    """ Program Serializer """

    class Meta:
        """ Meta Data """

        model = Program
        fields = ['id', 'url', ]


class CourseSerializer(HyperlinkedModelSerializer):
    """ Course Serializer """

    class Meta:
        """ Meta Data """

        model = Course
        fields = ['id', 'url', ]


class WeekSerializer(HyperlinkedModelSerializer):
    """ Week Serializer """

    class Meta:
        """ Meta Data """

        model = Week
        fields = ['id', 'url', ]


class SectionSerializer(HyperlinkedModelSerializer):
    """ Section Serializer """

    class Meta:
        """ Meta Data """

        model = Section
        fields = ['id', 'url', ]


class LectureSerializer(HyperlinkedModelSerializer):
    """ Lecture Serializer """

    class Meta:
        """ Meta Data """

        model = Lecture
        fields = ['id', 'url', ]
