from django.urls import path
from .views import (
    UserLoginView, 
    UserReisterView, 
    UserLogoutVeiw,
    delete_account,
    delete_course,
    delete_ticker,
    delete_comment,
    )

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login_user'),
    path('register/', UserReisterView.as_view(), name='register_user'),
    path('logout/', UserLogoutVeiw.as_view(), name='logout_user'),
    path('delete-account', delete_account, name='delete_account'),
    path('delete-course/<int:course_id>', delete_course, name='delete_course'),
    path('delete-ticker/<int:ticker_id>', delete_ticker, name='delete_ticker'),
    path('delete-comment/<int:comment_id>/<int:ticker_id>', delete_comment, name='delete_comment'),
]       