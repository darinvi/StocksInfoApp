from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import Ticker, Comment, Course
from stocks.stocks_auth.models import AppUser
from .forms import TickerModelForm, CommentModelForm, CourseModelForm
from django.urls import reverse_lazy, reverse
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import get_object_or_404


class TickerCreateView(CreateView):
    model = Ticker
    form_class = TickerModelForm
    template_name = 'forms/add_ticker.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class StrategyListView(views.ListView):
    model = Ticker
    template_name = 'lists/list_strategies.html'

    def get_queryset(self):    
        queryset = Ticker.objects.filter(show_public=True)
        return queryset

class UserProfile(auth_mixins.LoginRequiredMixin, views.ListView):
    model = Ticker
    template_name = 'profile.html'

    def get_queryset(self):
        user = self.request.user
        queryset = Ticker.objects.filter(user=user)
        return queryset
    

class CommentCreateView(auth_mixins.LoginRequiredMixin, views.CreateView, views.ListView):
    model = Comment
    form_class = CommentModelForm
    template_name = 'forms/comment_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ticker_pk'] = self.kwargs.get('ticker_pk')
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.ticker = get_object_or_404(Ticker, pk=self.kwargs['ticker_pk'])
        return super().form_valid(form)
    
    def get_queryset(self):
        ticker = get_object_or_404(Ticker, pk=self.kwargs['ticker_pk'])
        queryset = Comment.objects.filter(ticker=ticker)
        return queryset
    
    def get_success_url(self):
        return reverse_lazy('post_comment', kwargs={'ticker_pk': self.kwargs['ticker_pk']})
    
class UserDetails(views.ListView):
    model = Ticker
    template_name = 'lists/user_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_pk'] = self.kwargs.get('user_pk')
        return context
    
    def get_queryset(self):    
        user = get_object_or_404(AppUser, pk=self.kwargs['user_pk'])
        queryset = Ticker.objects.filter(user=user)
        return queryset
    
def delete_ticker(request, ticker_id):
    ticker = Ticker.objects.get(pk=ticker_id)
    if request.user.is_staff or request.user.is_superuser or ticker.user == request.user:
        ticker.delete()
    return redirect(reverse('list_strategies'))

def delete_comment(request, comment_id, ticker_id):
    comment = Comment.objects.get(pk=comment_id)
    if request.user.is_staff or request.user.is_superuser or comment.author == request.user:
        comment.delete()
    return redirect(reverse('post_comment', kwargs={'ticker_pk': ticker_id}))

class TickerDetails(views.ListView):
    model = Ticker
    template_name = 'lists/ticker_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ticker_name'] = self.kwargs.get('ticker_name')
        return context
    
    def get_queryset(self):    
        queryset = Ticker.objects.filter(ticker_name__iexact=self.kwargs['ticker_name'])
        return queryset
    
class MoreDetails(views.TemplateView):
    template_name = 'components/more_ticker_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ticker'] = Ticker.objects.get(pk=self.kwargs['ticker_id'])
        return context
    
class CourseFormView(auth_mixins.LoginRequiredMixin, views.CreateView):
    form_class = CourseModelForm
    model = Course
    template_name = 'forms/create_course.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CourseListView(views.ListView):
    template_name = 'lists/list_courses.html'
    model = Course

def create_content(request):
    return render(request, 'components/create_content.html')