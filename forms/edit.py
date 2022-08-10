from core_lms.models import *
from core_lms.forms.base import StyledModelForm
from django.contrib.auth.views import get_user_model

User = get_user_model()


class UserEditForm(StyledModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
