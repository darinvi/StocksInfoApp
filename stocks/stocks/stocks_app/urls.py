from django.urls import path
from .views import (
    TickerCreateView, 
    StrategyListView, 
    UserProfile, 
    CommentCreateView, 
    UserDetails, 
    TickerDetails,
    MoreDetails, 
    CourseListView,
    CourseFormView,
    delete_ticker, 
    delete_comment,
    create_content,
)


urlpatterns = [
    path('', TickerCreateView.as_view(), name='index'),
    path('create-ticker-strategy/', TickerCreateView.as_view(), name='create_strategy'),
    path('list-strategies', StrategyListView.as_view(),name='list_strategies'),
    path('profile/', UserProfile.as_view(), name='profile_user'),
    path('post-comment/<int:ticker_pk>', CommentCreateView.as_view(), name='post_comment'),
    path('user-details/<int:user_pk>', UserDetails.as_view(), name='user_details'),
    path('delete-ticker/<int:ticker_id>', delete_ticker, name='delete_ticker'),
    path('delete-comment/<int:comment_id>/<int:ticker_id>', delete_comment, name='delete_comment'),
    path('ticker-details/<slug:ticker_name>', TickerDetails.as_view(), name='ticker_details'),
    path('more-details/<int:ticker_id>', MoreDetails.as_view(), name='more_details'),
    path('courses', CourseListView.as_view(), name='list_courses'),
    path('course-create', CourseFormView.as_view(), name='create_course'),
    path('create-content', create_content, name='create_content'),
]

# TO DO: fix index page, currently having two paths doing the same