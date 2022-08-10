from django.db import models
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib.auth.models import AbstractUser


class BaseModel:
    """
    A mixin class to provide get_absolute_url method to model classes following the convention.
    Requires ListView names to be modelName_list.
    """

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        suffix = self._meta.verbose_name.lower()
        return reverse_lazy('core_lms:' + suffix + '_list')


# Create your models here.
class CoreUser(AbstractUser):
    image = models.ImageField(
        upload_to='users/images/',
        help_text='Profile image'
    )
    bio = models.CharField(
        max_length=128,
        help_text='Tell us about yourself'
    )


class Program(models.Model):
    title = models.CharField(
        unique=True,
        max_length=128,
        help_text='Program title'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Course(models.Model):
    specialization = models.ForeignKey(
        Program,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    title = models.CharField(
        unique=True,
        max_length=128,
        help_text='Course title'
    )
    about = models.CharField(
        max_length=1024,
        help_text='Short description of the course'
    )
    description = models.TextField(
        help_text='Course description'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Week(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=128,
        help_text='Week title'
    )
    about = models.CharField(
        max_length=1204,
        help_text='Short description of the week'
    )


class Section(models.Model):
    week = models.ForeignKey(
        Week,
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=128,
        help_text='Section title'
    )


class Lecture(models.Model):
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=128,
        help_text='Lecture title'
    )
    content = models.TextField(
        null=True,
        blank=True,
        help_text='Lecture content'
    )
    video = models.FileField(
        upload_to='lectures/videos/'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Member(models.Model):
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
        unique_together = ('user', 'course')
