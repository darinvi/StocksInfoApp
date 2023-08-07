from django.contrib.auth import views as auth_views
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.views import generic as views
from stocks.stocks_app.models import Profile, Course, Ticker, Comment
from django import forms
from django.urls import reverse_lazy
from django.urls import reverse
from django.shortcuts import render, redirect

UserModel = get_user_model()

class UserRegisterForm(auth_forms.UserCreationForm):    
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
    )
    accept = forms.BooleanField()

    def save(self, commit=True):
        user = super().save(commit)
        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            user = user,  
        )
        if commit:
            profile.save()
        return user

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields =('email',)

class UserLoginView(auth_views.LoginView):
    template_name = 'auth/login.html'

class UserReisterView(views.CreateView):
    template_name = 'auth/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result

class UserLogoutVeiw(auth_views.LogoutView):
    pass

def delete_account(request):
    user = UserModel.objects.get(pk=request.user.pk)
    logout(request)
    user.delete()
    return redirect(reverse('login_user'))

def delete_course(request, course_id):
    course = Course.objects.get(pk=course_id)
    if course.author.pk == request.user.pk:
        course.delete()
    return redirect(reverse('list_courses'))

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