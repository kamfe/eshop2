from django.views.generic.edit import UpdateView

from allauth.account.views import SignupView, LoginView

from users.models import MyUser
from users.forms import ChangeProfileForm


class CustomSignupView(SignupView):
    template_name = 'users/signup.html'
    success_url = '/'


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    success_url = '/'
# I didn't override all views. It's simple, but useless and long


class ProfilePageView(UpdateView):
    template_name = 'users/profile.html'
    model = MyUser
    form_class = ChangeProfileForm
