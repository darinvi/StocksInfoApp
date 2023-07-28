from django.urls import path
from .views import UserLoginView, UserReisterView, UserLogoutVeiw

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login_user'),
    path('register/', UserReisterView.as_view(), name='register_user'),
    path('logout/', UserLogoutVeiw.as_view(), name='logout_user'),
    # path('edit-profile/'),
]   