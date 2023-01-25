from django.urls import path, include
from users.views import CustomSignupView, CustomLoginView , ProfilePageView
urlpatterns = [
    # I didn't override all allauth urls. It's simple, but useless and long
    path('signup/', CustomSignupView.as_view()),
    path('login/', CustomLoginView.as_view()),
    path('', include('allauth.urls')),
    path('profile/<int:pk>/', ProfilePageView.as_view(), name='profile'),
]

