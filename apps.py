""" App Configuration """


from django.apps import AppConfig


class CoreLMSConfig(AppConfig):
    """ Configuration for the LMS """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core_lms'
