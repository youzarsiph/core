from django.urls import path
from core_lms.forms.main import *
from core_lms.views.main import *
from django.urls import reverse_lazy
from django.contrib.auth import views

app_name = 'core_lms'
main_patterns = [
    # Public views
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('learn/', ProgramListView.as_view(), name='learn'),

    # Programs

    # Courses
    path('courses/', CourseListView.as_view(), name='courses'),
    path('courses/<int:id>/', CourseDetailView.as_view(), name='course_detail'),

    # Administration views
    # Programs
    path('dashbaord/', DashboardView.as_view(), name='dashboard'),
    path('dashbaord/programs/', ProgramListView.as_view(), name='program_list'),
    path('dashboard/programs/new/', ProgramCreationView.as_view(), name='create_program'),
    path('dashboard/programs/<int:id>/edit/', ProgramEditView.as_view(), name='edit_program'),
    path('dashboard/programs/<int:id>/delete/', ProgramDeletionView.as_view(), name='delete_program'),

    # Courses
    path('dashbaord/courses/', CourseListView.as_view(), name='course_list'),
    path('dashboard/courses/new/', CourseCreationView.as_view(), name='create_course'),
    path('dashboard/courses/<int:id>/edit/', CourseEditView.as_view(), name='edit_course'),
    path('dashboard/courses/<int:id>/delete/', CourseDeletionView.as_view(), name='delete_course'),

]

auth_patterns = [
    # Custom authentication patterns
    path(
        'accounts/login/',
        views.LoginView.as_view(
            form_class=StyledAuthenticationForm,
            template_name='core_lms/authentication/login.html',
            extra_context={
                'signup_form': StyledUserCreationForm()
            }
        ),
        name='login'
    ),
    path(
        'accounts/register/',
        UserCreationView.as_view(),
        name='register'
    ),
    path(
        'accounts/<int:id>/edit/',
        UserEditView.as_view(),
        name='edit_user'
    ),
    path(
        'accounts/<int:id>/delete/',
        UserDeletionView.as_view(),
        name='delete_user'
    ),
    path(
        'accounts/logout/',
        views.LogoutView.as_view(
            template_name='core_lms/authentication/logged_out.html'
        ),
        name='logout'
    ),
    path(
        'accounts/profile/',
        ProfileView.as_view(),
        name='profile'
    ),
    path(
        'accounts/password/change/',
        views.PasswordChangeView.as_view(
            form_class=StyledPasswordChangeForm,
            template_name='core_lms/authentication/change_password.html',
            success_url=reverse_lazy('core_lms:change_done')
        ),
        name='change_password'
    ),
    path(
        'accounts/password/change/done/',
        views.PasswordChangeDoneView.as_view(
            template_name='core_lms/authentication/change_done.html'
        ),
        name='change_done'
    ),
    path(
        'accounts/password/reset/',
        views.PasswordResetView.as_view(
            form_class=StyledPasswordResetForm,
            template_name='core_lms/authentication/reset_password.html',
            success_url=reverse_lazy('core_lms:reset_done')
        ),
        name='reset_password'
    ),
    path(
        'accounts/password/reset/done/',
        views.PasswordResetDoneView.as_view(
            template_name='core_lms/authentication/reset_done.html'
        ),
        name='reset_done'
    ),
    path(
        'accounts/password/reset/confirm/<uidb64>/<token>/',
        views.PasswordResetConfirmView.as_view(
            template_name='core_lms/authentication/reset_confirm.html',
            form_class=StyledPasswordResetForm,
            success_url=reverse_lazy('core_lms:reset_complete')
        ),
        name='reset_confirm'
    ),
    path(
        'accounts/password/reset/complete/',
        views.PasswordResetCompleteView.as_view(
            template_name='core_lms/authentication/reset_complete.html',
        ),
        name='reset_complete'
    ),
]

urlpatterns = main_patterns + auth_patterns
