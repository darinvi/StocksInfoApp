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
    TransactionListView,
    CompleteTransactionHistoryListView,
    create_content,
    stock_data,
    create_transaction
)


urlpatterns = [
    path('', StrategyListView.as_view(), name='index'),
    path('create-ticker-strategy/', TickerCreateView.as_view(), name='create_strategy'),
    path('list-strategies', StrategyListView.as_view(),name='list_strategies'),
    path('profile/', UserProfile.as_view(), name='profile_user'),
    path('post-comment/<int:ticker_pk>', CommentCreateView.as_view(), name='post_comment'),
    path('user-details/<int:user_pk>', UserDetails.as_view(), name='user_details'),
    path('ticker-details/<slug:ticker_name>', TickerDetails.as_view(), name='ticker_details'),
    path('more-details/<int:ticker_id>', MoreDetails.as_view(), name='more_details'),
    path('courses', CourseListView.as_view(), name='list_courses'),
    path('course-create', CourseFormView.as_view(), name='create_course'),
    path('create-content', create_content, name='create_content'),
    path('stock-data/<slug:ticker_name>', stock_data, name='stock_data'),
    path('stock-data', stock_data, name='stock_data_input'),
    path('create-transaction', create_transaction, name='create_transaction'),
    path('list-transactions/<slug:ticker_name>/<int:user_pk>', TransactionListView.as_view(), name='list_transactions'),
    path('list-all-transactions/<int:user_pk>', CompleteTransactionHistoryListView.as_view(), name='list_all_transactions'),
]

# TO DO: fix index page, currently having two paths doing the same