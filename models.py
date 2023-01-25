""" Data Models """


from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    """ User Model """

    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='users/images/',
        help_text='Profile image'
    )
    bio = models.CharField(
        null=True,
        blank=True,
        max_length=128,
        help_text='Tell us about yourself'
    )


class Program(models.Model):
    """ Program Model """

    # The teacher of the program
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    title = models.CharField(
        unique=True,
        max_length=128,
        help_text='Program title (Required)'
    )
    about = models.CharField(
        max_length=1024,
        help_text='Short description of the program (Required)'
    )
    description = models.TextField(
        help_text='Program description (Required)'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Course(models.Model):
    """ Course Model """

    # The teacher of the course
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    # The program that the course belongs to
    program = models.ForeignKey(
        Program,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    title = models.CharField(
        unique=True,
        db_index=True,
        max_length=128,
        help_text='Course title (Required)',
    )
    about = models.CharField(
        max_length=1024,
        help_text='Short description of the course (Required)'
    )
    description = models.TextField(
        help_text='Course description (Required)'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Week(models.Model):
    """ Week Model """

    # The course that the course belongs to
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=128,
        db_index=True,
        help_text='Week title (Required)'
    )
    about = models.CharField(
        max_length=1204,
        help_text='Short description of the week (Required)'
    )

    def __str__(self):
        return self.course.title + ' > ' + self.title


class Section(models.Model):
    """ Section Model """

    # The week that the section belongs to
    week = models.ForeignKey(
        Week,
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=128,
        db_index=True,
        help_text='Section title (Required)'
    )

    def __str__(self):
        return self.week.course.title + ' > ' + self.week.title + ' > ' + self.title


class Lesson(models.Model):
    """ Lesson Model """

    # The section that the lesson belongs to
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=128,
        db_index=True,
        help_text='Lecture title (Required)'
    )
    content = models.TextField(
        null=True,
        blank=True,
        help_text='Lecture content'
    )
    video = models.FileField(
        null=True,
        blank=True,
        upload_to='lectures/videos/'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        lecture = self.section.week.course.title + ' > ' + \
            self.section.week.title + ' > ' + self.section.title + ' > '
        lecture += self.title
        return lecture


class Member(models.Model):
    """ Member Model """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Meta Data """

        unique_together = ('user', 'course')

    def __str__(self):
        return str(self.user) + '<-+->' + str(self.course)
